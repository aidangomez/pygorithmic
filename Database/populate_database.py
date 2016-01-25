from datetime import datetime

from Database import database
from Resource.enumerations import SortingOrder
from Resource.objects import Time
from Questrade import market_fetcher


def populate(db, symbol, start_date, end_date=Time.now()):
    columns = ["timestamp", "open", "close", "high", "low", "volume"]
    db.create_table(symbol, columns)

    if db.row_count(symbol) > 0:
        db.sort(symbol, "timestamp", SortingOrder.descending)
        latest_timestamp = db.next()["timestamp"]
        latest_time = Time(timestamp=latest_timestamp)

        if latest_time > start_date:
            start_date = latest_time + 1

    batch_start_time = start_date
    batch_end_time = start_date + 1000
    while (batch_end_time < end_date):
        quotes = market_fetcher.stock_quotes(symbol, batch_start_time,
                                             batch_end_time)
        for quote in quotes:
            timestamp = quote["start"]
            open = quote["open"]
            close = quote["close"]
            high = quote["high"]
            low = quote["low"]
            volume = quote["volume"]
            db.insert_unique(symbol, [timestamp, open, close, high, low,
                                      volume])
        batch_start_time += 1000
        batch_end_time += 1000

    if batch_start_time < end_date:
        quotes = market_fetcher.stock_quotes(symbol, batch_start_time,
                                             end_date)
        for quote in quotes:
            timestamp = quote["start"]
            open = quote["open"]
            close = quote["close"]
            high = quote["high"]
            low = quote["low"]
            volume = quote["volume"]
            db.insert_unique(symbol, [timestamp, open, close, high, low,
                                      volume])

    db.sort(symbol, "timestamp")
