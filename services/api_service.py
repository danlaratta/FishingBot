import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from FishingBot.point_systems.point_calculator import PointCalculator
from FishingBot.point_systems.point_system import PointSystem


class ApiService:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")
        self.weather_base_url = os.getenv("WEATHER_BASE_URL")

        if not self.weather_api_key or not self.weather_base_url:
            raise ValueError("Weather API_KEY or BASE_URL is missing in the .env file.")


    # Get the headers for api request
    def get_weather_headers(self):
        return {
            "Authorization": f"Bearer {self.weather_api_key}",
            "Content-Type": "application/json",
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


    # Create Dataframe with hourly models and return it
    def create_hourly_dataframe(self, endpoint, params=None):
        # Get the weather data
        data = self.get_weather_data(endpoint, params)

        if not data:
            print("No models available to create DataFrame.")
            return None

        # Extract hourly and moon data
        hourly_data = data["forecast"]["forecastday"][0]["hour"]
        moon_phase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

        # Create dataframe using list comprehension
        df = pd.DataFrame([
            {
                # "date": pd.to_datetime(hour["time"], format='%Y-%m-%d %H:%M').date(),
                # "hour": datetime.strptime(hour["time"], "%Y-%m-%d %H:%M").strftime("%l%p"), # parse time into datetime and extract hour
                "date_time": pd.to_datetime(hour["time"], format='%Y-%m-%d %H:%M'),
                "wind_speed": hour["wind_mph"],
                "wind_direction": hour["wind_dir"],
                "air_temp": hour["temp_f"],
                "weather_condition": hour["condition"]["text"],
                "moon_phase": moon_phase
            }
            for hour in hourly_data
        ])

        return df


    # Returns dataframe with point calculations
    def get_dataframe(self):
        api_service = ApiService()
        weather_endpoint = 'forecast.json'
        params = {
            'key': self.weather_api_key,
            'q': '08735'
        }

        # Creates dataframe with data returned from api
        df = api_service.create_hourly_dataframe(weather_endpoint, params=params)

        point_system = PointSystem()
        calculator = PointCalculator(df, point_system)

        # Runs point calculations and adds them to the dataframe
        df_calculated = calculator.process_calculations()
        return df_calculated
