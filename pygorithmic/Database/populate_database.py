from datetime import datetime

from . import database
from ..Resource.enumerations import SortingOrder
from ..Resource.objects import Time
from ..Questrade import market_fetcher


def populate(db, symbol, start_date, end_date=Time.now()):
    columns = ["timestamp", "open", "close", "high", "low", "volume"]
    db.create_table(symbol, columns)

    if db.row_count(symbol) > 0:
        db.sort(symbol, "timestamp", SortingOrder.descending)
        latest_timestamp = db.next()["timestamp"]
        latest_time = Time(timestamp=latest_timestamp)

        if latest_time > start_date:
            start_date = latest_time + 1

    def add_to_database(quotes):
        for quote in quotes:
            timestamp = quote["start"]
            open = quote["open"]
            close = quote["close"]
            high = quote["high"]
            low = quote["low"]
            volume = quote["volume"]
            db.insert_unique(symbol, [timestamp, open, close, high, low,
                                      volume])

    market_fetcher.fetch_market_data(symbol, start_date, end_date=end_date,
                      action=add_to_database)

    db.sort(symbol, "timestamp")
