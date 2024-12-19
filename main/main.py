from api_service.api_service import ApiService
import os
import requests
from dotenv import load_dotenv
import pandas as pd

class Main:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")

    def call_api(self):
        api_service = ApiService()

        params = {
            "key": self.api_key,
            "q": "08735"
        }

        data = api_service.get_non_hourly_data("marine.json", params=params)
        print(data)


main = Main()
main.call_api()