import requests
import os
from dotenv import load_dotenv

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api_key = os.getenv("WEATHER_API_KEY")



