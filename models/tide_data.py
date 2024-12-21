from datetime import datetime

class TideData:
    def __init__(self, water_temp: int, wave_height: float, high_tide_time: str, low_tide_time: str):
        self.water_temp = water_temp
        self.wave_height = wave_height

        try:
            parsed_high_tide_time = datetime.strptime(high_tide_time, "%b%-d%Y %I:%M%p")
            parsed_low_tide_time = datetime.strptime(low_tide_time, "%b%-d%Y %I:%M%p")
            self.high_tide_time = parsed_high_tide_time
            self.low_tide_time = parsed_low_tide_time
        except ValueError:
            raise ValueError("Invalid time format. Expected 'MM-DD-YYYY HH:MM'")
