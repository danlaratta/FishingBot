from datetime import datetime

class PointSystem:
    # Wind Speed (Moderately Important) – Max 6 points
    @staticmethod
    def wind_speed_points(wind_speed):
        if wind_speed < 0:
            raise ValueError("Wind speed cannot be below zero.")

        if wind_speed in range(5, 11):
            return 6
        elif wind_speed in range(10, 16):
            return 5
        elif wind_speed in range(0, 6) or wind_speed in range(15, 21):
            return 4
        elif wind_speed in range(20, 26):
            return 2
        elif wind_speed > 25:
            return 1
        return 0


    # Wind Direction (Moderately Important) – Max 6 points
    @staticmethod
    def wind_direction_points(wind_direction):
        if wind_direction in ["W", "NW"]:
            return 6
        elif wind_direction in ["N", "NE"]:
            return 4
        elif wind_direction == "E":
            return 3
        elif wind_direction in ["S", "SW", "SE"]:
            return 1
        return 0


    # Air Temperature (Less Important) – Max 4 points
    @staticmethod
    def air_temp_points(air_temp):
        if air_temp in range(55, 71):
            return 4
        elif air_temp in range(45, 55) or air_temp in range(71, 76):
            return 3
        elif air_temp in range(40, 45) or air_temp in range(76, 81):
            return 2
        elif air_temp < 40 or air_temp > 80:
            return 1
        return 0


    # General Weather (Moderately Important) – Max 6 points
    @staticmethod
    def weather_condition_points(weather_condition):
        if weather_condition.lower() == "light drizzle":
            return 6
        elif weather_condition.lower() in ["overcast", "partly cloudy", "light rain"]:
            return 5
        elif weather_condition.lower() in ["sunny", "clear"]:
            return 4
        elif weather_condition.lower() in ["Patchy rain nearby", "light snow"]:
            return 3
        elif weather_condition.lower() in ["moderate rain", "light snow showers"]:
            return 2
        elif weather_condition.lower() in ["heavy rain", "moderate snow", "heavy snow"]:
            return 1
        return 0


    # Hours to Tide Change (Moderately Important) – Max 6 points
    @staticmethod
    def hours_to_tide_change_points(num_hours):
        if 0 <= num_hours < 1:
            return 6
        elif 1 <= num_hours < 2:
            return 5
        elif 2 <= num_hours < 3:
            return 4
        elif 3 <= num_hours < 4:
            return 3
        elif 4 <= num_hours < 5:
            return 2
        elif 5 <= num_hours < 6:
            return 1

        return 0


    # Moon Phase (Moderately Important) – Max 6 points
    @staticmethod
    def moon_phase_points(moon_phase):
        if moon_phase.lower() in ["new moon", "full moon"]:
            return 6
        elif moon_phase.lower() in ["waxing gibbous", "waning gibbous"]:
            return 5
        elif moon_phase.lower() in ["first quarter", "last quarter"]:
            return 4
        elif moon_phase.lower() in ["waxing crescent", "waning crescent"]:
            return 2

        return 1


    # Time of Year (Most Important) – Max 10 points
    @staticmethod
    def time_of_year_points(date):
        current_year = date.year

        date_ranges = [
            (datetime(current_year, 9, 1), datetime(current_year, 11, 30), 10),  # Fall run
            (datetime(current_year, 5, 1), datetime(current_year, 5, 31), 8),  # Late spring
            (datetime(current_year, 3, 15), datetime(current_year, 4, 30), 6),  # Early spring
            (datetime(current_year, 12, 1), datetime(current_year, 12, 15), 4),  # Early winter
            (datetime(current_year, 12, 16), datetime(current_year, 12, 30), 3),  # Mid-winter
            (datetime(current_year, 6, 1), datetime(current_year, 8, 31), 2),  # Summer
            (datetime(current_year, 1, 1), datetime(current_year, 1, 15), 2),  # Early January
            (datetime(current_year, 1, 16), datetime(current_year, 3, 14), 1),  # Late winter
        ]
        # Check which date range the current date falls into
        for start_date, end_date, points in date_ranges:
            if start_date <= date <= end_date:
                return points

        return 0
