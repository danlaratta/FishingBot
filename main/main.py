import os
from dotenv import load_dotenv

from FishingBot.api_service.api_service import ApiService
from FishingBot.point_systems.point_calculator import PointCalculator
from FishingBot.point_systems.point_system import PointSystem


class Main:
    # Load environment variables
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv('WEATHER_API_KEY')

    def get_dataframe(self):
        # Initialize ApiService
        api_service = ApiService()
        
        # Endpoints
        weather_endpoint = 'forecast.json'


        params = {
            'key': self.weather_api_key,
            'q': '08735'
        }

        data = api_service.create_hourly_dataframe(weather_endpoint, params=params)
        return data


    def get_overall_day_percent(self):
        df = self.get_dataframe()
        if df is None:
            print('No DataFrame with data')
            return

        point_system = PointSystem()
        calculator = PointCalculator(df, point_system)

        # Run calculations
        df_calculated = calculator.process_all()
        print(df.to_string())
        # print(df_calculated.to_string())

main = Main()
main.get_overall_day_percent()