from datetime import datetime

from Database import database
from Resource.enumerations import SortingOrder
from Resource.objects import Time
from Questrade import market_fetcher


def populate(db, symbol, startDate):
    columns = ["timestamp", "open", "close", "high", "low", "volume"]
    db.createTable(symbol, columns)

    db.sort(symbol, "timestamp", SortingOrder.Descending)
    latestTimeStamp = db.next()["timestamp"]
    latestTime = Time(timestamp=latestTimeStamp)

    if latestTime > startDate:
        startDate = latestTime + 1

    endDate = startDate + 1000
    while (endDate < datetime.now()):
        quotes = market_fetcher.stockQuotes(symbol, startDate, endDate)
        for quote in quotes:
            timestamp = quote["start"]
            open = quote["open"]
            close = quote["close"]
            high = quote["high"]
            low = quote["low"]
            volume = quote["volume"]
            db.insertUnique(symbol, [timestamp, open, close, high, low,
                                     volume])
        startDate += 1000
        endDate += 1000

    endDate.date = datetime.now()
    quotes = market_fetcher.stockQuotes(symbol, startDate, endDate)
    for quote in quotes:
        timestamp = quote["start"]
        open = quote["open"]
        close = quote["close"]
        high = quote["high"]
        low = quote["low"]
        volume = quote["volume"]
        db.insertUnique(symbol, [timestamp, open, close, high, low, volume])

    db.sort(symbol, "timestamp")
