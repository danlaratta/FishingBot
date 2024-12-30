import os
import requests
from dotenv import load_dotenv
import pandas as pd

from FishingBot.api_service.api_service import ApiService


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

        data = api_service.create_hourly_dataframe("forecast.json", params=params)
        # data = api_service.create_non_hourly_dataframe("forecast.json", "tides", params=params)
        print(data)

        # ps = PointSystem()
        # calculator = PointCalculator()
        # print(calculator.calculate_condition_percentage(ps))

main = Main()
main.call_api()