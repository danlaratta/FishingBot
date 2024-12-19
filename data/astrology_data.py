from datetime import datetime

class AstrologyData:
    def __init__(self, moon_phase: str, current_date: str):
        self.moon_phase = moon_phase
        self.date_ranges = [
            (datetime.fromisoformat("Sep 1"), datetime.fromisoformat("Nov 30")),  # 10pts
            (datetime.fromisoformat("May 1"), datetime.fromisoformat("May 31")),  # 8pts
            (datetime.fromisoformat("Mar 15"), datetime.fromisoformat("Apr 30")), # 6pts
            (datetime.fromisoformat("Dec 1"), datetime.fromisoformat("Dec 15")),  # 4pts
            (datetime.fromisoformat("Dec 16"), datetime.fromisoformat("Dec 30")), # 3pts
            (datetime.fromisoformat("Jun 1"), datetime.fromisoformat("Aug 31")),  # 2pts
            (datetime.fromisoformat("Jan 1"), datetime.fromisoformat("Jan 15")),  # 2pts
            (datetime.fromisoformat("Jan 16"), datetime.fromisoformat("Mar 14")), # 1pt
        ]

        # Parse the string data returned from api extracting the month and day (year is not needed)
        try:
            parsed_date = datetime.strptime(current_date, "%Y-%m-%d").date() # parse full date
            self.month = parsed_date.month # extract month
            self.day = parsed_date.day     # extract day
        except ValueError:
            raise ValueError("Invalid date format. Expected 'yyyy-mm-dd'.")


