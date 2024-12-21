
class WeatherData:
    def __init__(self, wind_speed: int, wind_direction: str, air_temp: int, weather_condition: str):
        # ensures that the class is never instantiated with invalid models for wind_speed
        if wind_speed < 0:
            raise ValueError("Wind speed cannot be below zero.")

        if wind_direction not in ["N", "NE", "NW", "S", "SE", "SW", "W", "E"]:
            raise ValueError("Invalid wind direction")

        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.air_temp = air_temp
        self.weather_condition = weather_condition
