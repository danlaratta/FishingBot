from datetime import datetime

class TideData:
    def __init__(self, high_tide_time_am, high_tide_time_pm, low_tide_time_am, low_tide_time_pm):
        self.high_tide_time_am = high_tide_time_am
        self.high_tide_time_pm = high_tide_time_pm
        self.low_tide_time_am = low_tide_time_am
        self.low_tide_time_pm = low_tide_time_pm
        # self.water_temp = water_temp
        # self.wave_height = wave_height
