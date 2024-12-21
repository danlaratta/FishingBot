from datetime import datetime

class AstrologyData:
    def __init__(self, moon_phase: str):
        self.moon_phase = moon_phase
        self.current_year = datetime.today().year
        self.date_ranges = [
            (datetime(self.current_year, 9, 1), datetime(self.current_year, 11, 30), 10),  # 10pts
            (datetime(self.current_year, 5, 1), datetime(self.current_year, 5, 31), 8),  # 8pts
            (datetime(self.current_year, 3, 15), datetime(self.current_year, 4, 30), 6),  # 6pts
            (datetime(self.current_year, 12, 1), datetime(self.current_year, 12, 15), 4),  # 4pts
            (datetime(self.current_year, 12, 16), datetime(self.current_year, 12, 30), 3),  # 3pts
            (datetime(self.current_year, 6, 1), datetime(self.current_year, 8, 31), 2),  # 2pts
            (datetime(self.current_year, 1, 1), datetime(self.current_year, 1, 15), 2),  # 2pts
            (datetime(self.current_year, 1, 16), datetime(self.current_year, 3, 14), 1),  # 1pt
        ]
