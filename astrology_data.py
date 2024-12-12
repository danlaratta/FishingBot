from datetime import datetime


class AstrologyData:
    def __init__(self, moon_phase: str, time_of_year: str):
        self.moon_phase = moon_phase

        # Parse the string data returned from api extracting the month and day (year is not needed)
        try:
            parsed_date = datetime.strptime(time_of_year, "%Y-%m-%d").date() # parse full date
            self.month = parsed_date.month # extract month
            self.day = parsed_date.day     # extract day
        except ValueError:
            raise ValueError("Invalid date format. Expected 'yyyy-mm-dd'.")
