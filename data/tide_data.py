from datetime import date, datetime, time

class TideData:
    def __init__(self, water_temp: int, wave_height: float, high_tide_time: str, low_tide_time: str):
        self.water_temp = water_temp
        self.wave_height = wave_height

        try:
            parsed_high_tide_time = datetime.strptime(high_tide_time, "%I:%M%p").time()
            parsed_low_tide_time = datetime.strptime(low_tide_time, "%I:%M%p").time()
            self.high_tide_time = parsed_high_tide_time
            self.low_tide_time = parsed_low_tide_time
        except ValueError:
            raise ValueError("Invalid time format. Expected 'HH:MM'.")


