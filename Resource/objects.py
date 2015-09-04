class Quote:
    def __init__(self, quote):
        self.start = quote["start"]
        self.end = quote["end"]
        self.low = quote["low"]
        self.high = quote["high"]
        self.open = quote["open"]
        self.close = quote["close"]
        self.volume = quote["volume"]

class Time(str):
    def __new__(cls, year, month, day, hour="00", min="00", sec="00"):
        string = '-'.join([year, month, day]) + "T" + ":".join([hour, min, sec]) + "-05:00"
        return str.__new__(cls, string)
