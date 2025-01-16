from FishingBot.point_systems.point_system import PointSystem

class PointCalculator:
    point_system: PointSystem = None
    max_points = 36


    # calculate wind speed points
    @classmethod
    def calculate_wind_speed_points(cls):
        return cls.point_system.wind_speed_points()


    # calculate wind direction points
    @classmethod
    def calculate_wind_direction_points(cls):
        return cls.point_system.wind_direction_points()


    # calculate air temp points
    @classmethod
    def calculate_air_temp_points(cls):
        return cls.point_system.air_temp_points()


    # calculate weather condition points
    @classmethod
    def calculate_weather_condition_points(cls):
        return cls.point_system.weather_condition_points()



    # calculate moon phase points
    @classmethod
    def calculate_moon_phase_points(cls):
        return cls.point_system.moon_phase_points()


    # calculate time of year points
    @classmethod
    def calculate_time_of_year_points(cls):
        return cls.point_system.time_of_year_points()


    # calculate total points and fishing condition percentage
    @classmethod
    def calculate_condition_percentage(cls):
        wind_speed = cls.calculate_wind_speed_points()
        wind_direction = cls.calculate_wind_direction_points()
        air_temp = cls.calculate_air_temp_points()
        weather_condition = cls.calculate_weather_condition_points()
        moon_phase = cls.calculate_moon_phase_points()
        time_of_year = cls.calculate_time_of_year_points()

        points = [wind_speed, wind_direction, air_temp, weather_condition, moon_phase, time_of_year]

        sum = 0
        for point in points:
            sum += point

        return sum / cls.max_points


    """
    calculate hour to tide change points
    def calculate_hour_to_tide_change_points(cls):
        return cls.point_system.hours_to_tide_change_points()
    """