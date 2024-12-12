from astrology_data import AstrologyData
from tide_data import TideData
from weather_data import WeatherData


class PointSystem:

    def __init__(self, weather: WeatherData, tide: TideData, astrology: AstrologyData):
        self.weather = weather
        self.tide = tide
        self.astrology = astrology

    def wind_speed_points(self):
        if self.weather.wind_speed < 0:
            raise ValueError("Wind speed cannot be below zero.")

        if self.weather.wind_speed in range(5, 11):
            return 5
        elif self.weather.wind_speed in range(10, 16):
            return 4
        elif self.weather.wind_speed in range(0, 6) or self.weather.wind_speed in range(15, 21):
            return 3
        elif self.weather.wind_speed in range(20, 26):
            return 2
        elif self.weather.wind_speed > 25:
            return 1

        return 0


    def wind_direction_points(self):
        if self.weather.wind_direction in ["NW", "W"]:
            return 4
        elif self.weather.wind_direction in ["NE", "N"]:
            return 3
        elif self.weather.wind_direction == "E":
            return 2
        elif self.weather.wind_direction in ["S", "SW", "SE"]:
            return 1

        return 0


    """
    •	5 pts: 55-70 (comfortable air temperatures for fishing and maintaining good water temperatures)
    •	4 pts: 45-55 or 70-75
    •	3 pts: 75-80 or 40-45
    •	2 pts: 35-40 or 80-85
    •	1 pt: Below 35 or above 85

"""
    def air_temp_points(self):
        # if self.weather.air_temp in range()
        pass

    def water_temp_points(self):
        pass


    def weather_condition_points(self):
        pass


    def water_condition_points(self):
        pass


    def hours_to_tide_change_points(self):
        pass


    def moon_phase_points(self):
        pass


    def time_of_year_points(self):
        pass

    """
    I am building a fishing bot used to notify my about surf fishing conditions whether it is a good or bad day to go surf fishing in new jersey specifically for striped bass (will eventually add other species but sticking with just striped bass for now). The bot will automate making api requests to receive live weather and tide data and compare it to my point system i create which consists of categories related to surf fishing conditions. based on the conditions received from the api they will be scored which will be tallied and get a percentage of how good/bad the fishing conditions are for the day. This is my current point system for my bot:
1. Wind Speed (Ideal: Moderate wind for water movement)
•	5 pts: 5-10 mph
•	4 pts: 10-15 mph
•	3 pts: 0-5 mph or 15-20 mph
•	2 pts: 20-25 mph
•	1 pt: 25+ mph (too strong, rough surf can make fishing challenging)
2. Wind Direction (Ideal: West or Northwest winds)
•	4pts: West or Northwest (blows offshore, clearer water, and better casting conditions)
•	3pts: North or Northeast
•	2pts: East
•	1pt: South, South East, South West
3. Air Temperature (Ideal: Cool to moderate temperatures)
•	5 pts: 55°F-70°F (comfortable air temperatures for fishing and maintaining good water temperatures)
•	4 pts: 45°F-55°F or 70°F-75°F
•	3 pts: 75°F-80°F or 40°F-45°F
•	2 pts: 35°F-40°F or 80°F-85°F
•	1 pt: Below 35°F or above 85°F
4. Water Temperature (Ideal: Depends on species, 55°F-65°F is best for striped bass and other trophies)
•	5 pts: 55°F-65°F
•	4 pts: 50°F-55°F or 65°F-70°F
•	3 pts: 45°F-50°F or 70°F-75°F
•	2 pts: 40°F-45°F or 75°F-80°F
•	1 pt: Below 40°F or above 80°F
5. Hours to Tide Change (Ideal: 2 hours before and after tide changes)
•	5 pts: 0-1 hour to high/low tide (peak feeding times)
•	4 pts: 1-2 hours to high/low tide
•	3 pts: 2-3 hours to high/low tide
•	2 pts: 3-4 hours to high/low tide
•	1 pts: More than 4 hours from tide change
6. General Weather (Cloud Cover and Precipitation)
•	5 pts: Overcast with light drizzle (perfect for low-light fishing conditions)
•	4 pts: Fully overcast
•	3 pts: Partly cloudy
•	2 pts: Clear skies
•	1 pt: Heavy rain or thunderstorms (unsafe and challenging conditions)
7. Wave Height (Ideal: Moderate waves for water movement, but not rough surf)
•	5 pts: 1-2 feet
•	4 pts: 2-3 feet
•	3 pts: 0-1 feet or 3-4 feet
•	2 pts: 4-5 feet
•	1 pt: Over 5 feet (strong surf makes fishing difficult)
8. Moon Phase (Ideal: New or Full Moon for stronger tides and feeding activity)
•	5 pts: Full Moon or New Moon
•	4 pts: Waxing Gibbous or Waning Gibbous
•	3 pts: First Quarter or Last Quarter
•	2 pts: Waxing Crescent or Waning Crescent
•	1 pt: No moon visibility (minimal tidal influence)
9. Time of year (month-day range)
•	3pts March 15 - April 30 
•	4pts May 1 - May 31 
•	2pts June 1 - August 31 
•	5pts: September 1 - November 30 
•	4pts December 1 - December 15 
•	3pts December 16 - December 31 
•	2pts January 1 - January 15 
•	1pts January 16 - March 14 

i feel my point system is a good start but it doesn't take into consideration that some factors/categories matter more than others, for example the time of year is very important due to the fact that striped bass migrate and are only in NJ waters during certain spring and fall months of the year. How can i update my scoring system to be more accurate by including these factors into my point system in an easy yet effective way? Give me an updated scoring system including these factors so it is more accurate. 
    
    """