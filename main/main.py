from api_service.api_service import ApiService
import os
import requests
from dotenv import load_dotenv
import pandas as pd

class Main:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")

    def call_api(self):
        api_service = ApiService()

        params = {
            "key": self.weather_api_key,
            "q": "08735"
        }

        # models = api_service.create_hourly_dataframe("forecast.json", params=params)
        data = api_service.create_non_hourly_dataframe("tides", params=None)
        print(data)


main = Main()
main.call_api()