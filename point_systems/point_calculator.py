
class PointCalculator:
    def __init__(self, df, point_system):
        self.df = df # Stores dataframe storing weather data
        self.point_system = point_system # stores the PointSystem instance


    # create and store calculated points in wind_speed_points column
    def calculate_wind_speed_points(self):
        self.df['wind_speed_points'] = self.df['wind_speed'].apply(self.point_system.wind_direction_points)


    # create and store calculated points in wind_direction_points column
    def calculate_wind_direction_points(self):
        self.df['wind_direction_points'] = self.df['wind_direction'].apply(self.point_system.wind_direction_points)


    # create and store calculated points in air_temp_points column
    def calculate_air_temp_points(self):
        self.df['air_temp_points'] = self.df['air_temp'].apply(self.point_system.air_temp_points)


    # create and store calculated points in weather_condition_points column
    def calculate_weather_condition_points(self):
        self.df['weather_condition_points'] = self.df['weather_condition'].apply(self.point_system.weather_condition_points)


    # create and store calculated points in moon_phase_points column
    def calculate_moon_phase_points(self):
        self.df['moon_phase_points'] = self.df['moon_phase'].apply(self.point_system.moon_phase_points)


    # create and store calculated points in time_of_year_points column
    def calculate_time_of_year_points(self):
        self.df['time_of_year_points'] = self.df['date_time'].apply(self.point_system.time_of_year_points)


    # calculate the percentage of good fishing time (e.g., hourly points over total points for the day)
    def calculate_hourly_percentages(self):
        self.df['total_points'] = (
                self.df['wind_direction_points'] +
                self.df['wind_speed_points'] +
                self.df['air_temp_points'] +
                self.df['weather_condition_points'] +
                self.df['moon_phase_points'] +
                self.df['time_of_year_points']
        )

        # max_points = self.df['hourly_points'].max()
        max_points = 38
        self.df['percentage'] = round(self.df['total_points'] / max_points * 100, 2)


    # process all calculations and return the dataframe
    def process_calculations(self):
        self.calculate_wind_direction_points()
        self.calculate_wind_speed_points()
        self.calculate_air_temp_points()
        self.calculate_weather_condition_points()
        self.calculate_moon_phase_points()
        self.calculate_time_of_year_points()
        self.calculate_hourly_percentages()
        return self.df
