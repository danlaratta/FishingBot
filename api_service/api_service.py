import os
from calendar import month

import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

from pandas.core.interchange.dataframe_protocol import DataFrame


class ApiService:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL")

        if not self.api_key or not self.base_url:
            raise ValueError("API_KEY or BASE_URL is missing in the .env file.")


    # Get the headers for api request
    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    # Get request to api
    def get_data(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()

        try:
            # Make request and return parsed json
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


    # Create Dataframe with hourly data and return it
    def get_hourly_data(self, endpoint, params=None):
        # Get the api data
        data = self.get_data(endpoint, params)

        if not data:
            print("No data available to create DataFrame.")
            return None

        # Extract hourly data
        hourly_data = data["forecast"]["forecastday"][0]["hour"]

        # Create dataframe using list comprehension
        df = pd.DataFrame([
            {
                "time": datetime.strptime(hour["time"], "%Y-%m-%d %H:%M").strftime("%l%p"), # parse time into datetime and extract hour
                "water_temp":hour["water_temp_f"],
                "wave_height": hour["swell_ht_ft"],
                "wind_direction": hour["wind_dir"],
                "air_temp": hour["temp_f"],
                "weather_condtion": hour["condition"]["text"],
            }
            for hour in hourly_data
        ])

        return df


    # Create Dataframe with non-hourly data and return it
    def get_non_hourly_data(self, endpoint, params=None):
        data = self.get_data(endpoint, params)

        if not data:
            print("No tide data available.")
            return None

        high_tide_am = data["forecast"]["forecastday"][0]["day"]["tides"][0]["tide"][0]["tide_time"]
        high_tide_pm = data["forecast"]["forecastday"][0]["day"]["tides"][0]["tide"][2]["tide_time"]
        low_tide_am = data["forecast"]["forecastday"][0]["day"]["tides"][0]["tide"][1]["tide_time"]
        low_tide_pm = data["forecast"]["forecastday"][0]["day"]["tides"][0]["tide"][3]["tide_time"]
        current_date = data["forecast"]["forecastday"][0]["date"]
        moon_phase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

        df = pd.DataFrame([
            {
                "date": datetime.strptime(current_date, "%Y-%m-%d").strftime("%b %d %Y"),
                "high_tide_am": datetime.strptime(high_tide_am, "%Y-%m-%d %H:%M").strftime("%I:%M%p"),
                "high_tide_pm": datetime.strptime(high_tide_pm, "%Y-%m-%d %H:%M").strftime("%I:%M%p"),
                "low_tide_am": datetime.strptime(low_tide_am, "%Y-%m-%d %H:%M").strftime("%I:%M%p"),
                "low_tide_pm": datetime.strptime(low_tide_pm, "%Y-%m-%d %H:%M").strftime("%I:%M%p"),
                "moon_phase": moon_phase
            }
        ])

        # test_date = datetime.fromisoformat("Sep 1")
        return df

