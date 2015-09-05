from datetime import datetime

from enumerations import Interval


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

    def __init__(self, year, month, day, hour="00", min="00", sec="00",
                 interval=Interval.OneDay.delta):
        self.date = datetime(year, month, day, hour, min, second)
        self.delta = interval

    def __repr__(self):
        return self.date.isoformat() + "-05:00"

    def __iadd__(self, b):
        self.date += b * self.delta
