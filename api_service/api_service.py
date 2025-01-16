import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime


class ApiService:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")
        self.tide_api_key = os.getenv("TIDE_API_KEY")
        self.weather_base_url = os.getenv("WEATHER_BASE_URL")
        self.tide_base_url = os.getenv("TIDE_BASE_URL")
        self.station_id = os.getenv("STATION_ID")

        if not self.weather_api_key or not self.weather_base_url:
            raise ValueError("Weather API_KEY or BASE_URL is missing in the .env file.")

        if not self.tide_api_key or not self.tide_base_url:
            raise ValueError("Tide API_KEY or BASE_URL is missing in the .env file.")

    # Get the headers for api request
    def get_weather_headers(self):
        return {
            "Authorization": f"Bearer {self.weather_api_key}",
            "Content-Type": "application/json",
        }


    def get_tide_headers(self):
        return {
            "x-rapidapi-key": self.tide_api_key,
        }


    # Get weather models
    def get_weather_data(self, endpoint, params=None):
        url = f"{self.weather_base_url}/{endpoint}"
        headers = self.get_weather_headers()

        try:
            # Make request and return parsed json
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


    # get tide and moon models
    def get_tide_data(self, endpoint, params=None):
        url = f"{self.tide_base_url}/stations/{self.station_id}/{endpoint}"
        headers = self.get_tide_headers()

        try:
            # Make request and return parsed json
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


    # Create Dataframe with hourly models and return it
    def create_hourly_dataframe(self, endpoint, params=None):
        # Get the api models
        data = self.get_weather_data(endpoint, params)

        if not data:
            print("No models available to create DataFrame.")
            return None

        # Extract hourly models
        hourly_data = data["forecast"]["forecastday"][0]["hour"]

        # Get moon phase
        moon_phase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

        # Create dataframe using list comprehension
        df = pd.DataFrame([
            {
                "date": pd.to_datetime(hour["time"], format='%Y-%m-%d %H:%M').date(),
                "hour": datetime.strptime(hour["time"], "%Y-%m-%d %H:%M").strftime("%l%p"), # parse time into datetime and extract hour
                "wind_speed": hour["wind_mph"],
                "wind_direction": hour["wind_dir"],
                "air_temp": hour["temp_f"],
                "weather_condition": hour["condition"]["text"],
                "moon_phase": moon_phase
            }
            for hour in hourly_data
        ])

        return df


    # Create Dataframe with non-hourly models and return it
    def create_non_hourly_dataframe(self, weather_endpoint, tide_endpoint, params=None):
        moon_data = self.get_weather_data(weather_endpoint, params)
        tide_data = self.get_tide_data(tide_endpoint, None)

        if not moon_data and not tide_data:
            print("No tide or moon models available.")
            return None

        df = pd.DataFrame(tide_data["tides"], columns=["date", "time", "type", "height"])
        moon_phase = moon_data["forecast"]["forecastday"][0]["astro"]["moon_phase"]
        df["moon_phase"] = moon_phase # add moon phase to dataframe
        return df

