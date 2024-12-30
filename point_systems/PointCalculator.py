from FishingBot.point_systems.point_system import PointSystem


class PointCalculator:
    def __init__(self, point_system: PointSystem):
        self.point_system = point_system
        self.max_points = 36 # NOTE: will change once finish point system for hours to tide


    # calculate wind speed points
    def calculate_wind_speed_points(self):
        return self.point_system.wind_speed_points()


    # calculate wind direction points
    def calculate_wind_direction_points(self):
        return self.point_system.wind_direction_points()


    # calculate air temp points
    def calculate_air_temp_points(self):
        return self.point_system.air_temp_points()


    # calculate weather condition points
    def calculate_weather_condition_points(self):
        return self.point_system.weather_condition_points()



    # calculate hour to tide change points
    # def calculate_hour_to_tide_change_points(self):
    #     return self.point_system.hours_to_tide_change_points()


    # calculate moon phase points
    def calculate_moon_phase_points(self):
        return self.point_system.moon_phase_points()


    # calculate time of year points
    def calculate_time_of_year_points(self):
        return self.point_system.time_of_year_points()


    # calculate total points and fishing condition percentage
    def calculate_condition_percentage(self):
        wind_speed = self.calculate_wind_speed_points()
        wind_direction = self.calculate_wind_direction_points()
        air_temp = self.calculate_air_temp_points()
        weather_condition = self.calculate_weather_condition_points()
        moon_phase = self.calculate_moon_phase_points()
        time_of_year = self.calculate_time_of_year_points()

        points = [wind_speed, wind_direction, air_temp, weather_condition, moon_phase, time_of_year]

        sum = 0
        for point in points:
            sum += point

        return sum / self.max_points