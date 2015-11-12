from datetime import datetime

from Database import database
from Questrade import market_fetcher


def populate(db, symbol, startDate):
    columns = ["timestamp", "open", "close", "high", "low", "volume"]
    db.createTable(symbol, columns)

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
            db.insert(symbol, [timestamp, open, close, high, low, volume])
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
        db.insert(symbol, [timestamp, open, close, high, low, volume])

    db.sort(symbol, "timestamp")
