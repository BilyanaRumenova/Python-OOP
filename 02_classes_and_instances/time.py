from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.datetime_object = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self):
        self.datetime_object += timedelta(seconds=1)
        self.hours = self.datetime_object.hour
        self.minutes = self.datetime_object.minute
        self.seconds = self.datetime_object.second
        return self.get_time()
