from datetime import datetime, tzinfo
import time

from .enumerations import Interval


class Quote:

    def __init__(self, quote):
        self.start = quote["start"]
        self.end = quote["end"]
        self.low = quote["low"]
        self.high = quote["high"]
        self.open = quote["open"]
        self.close = quote["close"]
        self.volume = quote["volume"]


class Time:

    @staticmethod
    def now():
        return Time(datetime_object=datetime.now())

    def __init__(self, datetime_object=None, timestamp=None, year=1, month=1,
                 day=1, hour=0, min=0, sec=0, interval=Interval.OneDay):
        if (datetime_object is not None):
            self.date = datetime_object
        elif (timestamp is None):
            self.date = datetime(year, month, day, hour, min, sec)
        else:
            time_object = time.strptime(timestamp[:19], "%Y-%m-%dT%H:%M:%S")
            self.date = datetime.fromtimestamp(time.mktime(time_object))
        self.interval = interval

    def __repr__(self):
        return self.date.isoformat() + "-05:00"

    def __add__(self, b):
        new_date = self.date + b * self.interval.delta
        new_time = Time(interval=self.interval)
        new_time.date = new_date
        return new_time

    def __iadd__(self, b):
        self.date += b * self.interval.delta
        return self

    def __lt__(self, b):
        return self.date < b

    def __le__(self, b):
        return self.date <= b

    def __eq__(self, b):
        return self.date == b

    def __ne__(self, b):
        return self.date != b

    def __gt__(self, b):
        return self.date > b

    def __ge__(self, b):
        return self.date >= b
