from datetime import datetime

from FishingBot.models.astrology_data import AstrologyData
from FishingBot.models.tide_data import TideData
from FishingBot.models.weather_data import WeatherData


class PointSystem:
    weather: WeatherData = None
    tide: TideData = None
    astrology: AstrologyData = None

    # Essentially init method for class instances
    @classmethod
    def populate_data(cls, weather, tide, astrology):
        cls.weather = weather
        cls.tide = tide
        cls.astrology = astrology


    # Wind Speed (Moderately Important) – Max 6 points
    @classmethod
    def wind_speed_points(cls) -> int:
        if cls.weather.wind_speed < 0:
            raise ValueError("Wind speed cannot be below zero.")

        if cls.weather.wind_speed in range(5, 11):
            return 6
        elif cls.weather.wind_speed in range(10, 16):
            return 5
        elif cls.weather.wind_speed in range(0, 6) or cls.weather.wind_speed in range(15, 21):
            return 4
        elif cls.weather.wind_speed in range(20, 26):
            return 2
        elif cls.weather.wind_speed > 25:
            return 1
        return 0


    # Wind Direction (Moderately Important) – Max 6 points
    @classmethod
    def wind_direction_points(cls) -> int:
        if cls.weather.wind_direction in ["W", "NW"]:
            return 6
        elif cls.weather.wind_direction in ["N", "NE"]:
            return 4
        elif cls.weather.wind_direction == "E":
            return 3
        elif cls.weather.wind_direction in ["S", "SW", "SE"]:
            return 1
        return 0


    # Air Temperature (Less Important) – Max 4 points
    @classmethod
    def air_temp_points(cls) -> int:
        if cls.weather.air_temp in range(55, 71):
            return 4
        elif cls.weather.air_temp in range(45, 55) or cls.weather.air_temp in range(71, 76):
            return 3
        elif cls.weather.air_temp in range(40, 45) or cls.weather.air_temp in range(76, 81):
            return 2
        elif cls.weather.air_temp < 40 or cls.weather.air_temp > 80:
            return 1
        return 0


    """
    # Water Temperature (Very Important) – Max 8 points
    def water_temp_points(cls) -> int:
        if cls.tide.water_temp in range(55, 66):
            return 8
        elif cls.tide.water_temp in range(50, 55) or cls.tide.water_temp in range(65, 71):
            return 6
        elif cls.tide.water_temp in range(45, 50) or cls.tide.water_temp in range(70, 76):
            return 4
        elif cls.tide.water_temp in range(40, 45) or cls.tide.water_temp in range(76, 81):
            return 2
        elif 40 > cls.tide.water_temp > 80:
            return 1
        return 0
    """


    # General Weather (Moderately Important) – Max 6 points
    @classmethod
    def weather_condition_points(cls) -> int:
        if cls.weather.weather_condition.lower() == "light drizzle":
            return 6
        elif cls.weather.weather_condition.lower() in ["overcast", "partly cloudy", "light rain"]:
            return 5
        elif cls.weather.weather_condition.lower() in ["sunny", "clear"]:
            return 4
        elif cls.weather.weather_condition.lower() in ["Patchy rain nearby", "light snow"]:
            return 3
        elif cls.weather.weather_condition.lower() in ["moderate rain", "light snow showers"]:
            return 2
        elif cls.weather.weather_condition.lower() in ["heavy rain", "moderate snow", "heavy snow"]:
            return 1
        return 0


    """
    # Wave Height or Water Conditions (Moderately Important) – Max 6 points
    def water_condition_points(cls) -> int:
        if 1.0 <= cls.tide.wave_height <= 2.0:
            return 6
        elif 2.1 <= cls.tide.wave_height <= 3.0:
            return 5
        elif 3.1 <= cls.tide.wave_height <= 4.0:
            return 4
        elif 4.1 <= cls.tide.wave_height <= 5.0:
            return 3
        elif 5.1 <= cls.tide.wave_height <= 6.0:
            return 2
        elif cls.tide.wave_height < 6.1:
            return 1
        return 0
    """

    # Hours to Tide Change (Moderately Important) – Max 6 points
    @classmethod
    def hours_to_tide_change_points(cls):
        current_datetime = datetime.now()
        return current_datetime



    # Moon Phase (Moderately Important) – Max 6 points
    @classmethod
    def moon_phase_points(cls) -> int:
        if cls.astrology.moon_phase.lower() in ["new moon", "full moon"]:
            return 6
        elif cls.astrology.moon_phase.lower() in ["waxing gibbous", "waning gibbous"]:
            return 5
        elif cls.astrology.moon_phase.lower() in ["first quarter", "last quarter"]:
            return 4
        elif cls.astrology.moon_phase.lower() in ["waxing crescent", "waning crescent"]:
            return 2

        return 1


    # Time of Year (Most Important) – Max 10 points
    @classmethod
    def time_of_year_points(cls) -> int:
        current_date = datetime.today()

        for start_date, end_date, points in cls.astrology.date_ranges:
            if start_date <= current_date <= end_date:
                return points

        return 0


