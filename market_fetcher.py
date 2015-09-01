import sqlite3

import questrade_request
from Resource.enumerations import Time, RequestType
from Resource.objects import Quote


def stockQuotes(symbol, startDate, endDate, timeFrame):
    """
    dates povided in string as "year-month-day"
    """
    request = questrade_request.MarketRequest()
    stockList = request.get(RequestType.Market.searchSymbol,
                             params={"prefix": symbol})
    stockId = stockList["symbols"][0]["symbolId"]

    startDate = startDate + "T00:00:00-05:00"
    endDate = endDate + "T00:00:00-05:00"

    return request.get(RequestType.Market.getQuotes(stockId),
                        params={"startTime": startDate,
                                "endTime": endDate,
                                "interval": timeFrame})["candles"]


def populateDB(stockname, quotes):
    connection = sqlite3.connect("quotes.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS {} (start, end, low, high, open,\
        close, volume)".format(stockname))

    quoteList = []
    for quote in quotes:
        tempQuote = Quote(quote)
        quoteList.append(tempQuote)

        cursor.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?)".format(stockname),
                       (tempQuote.start, tempQuote.end, tempQuote.low,
                        tempQuote.high, tempQuote.open, tempQuote.close, tempQuote.volume))

    connection.commit()
    cursor.close()
    connection.close()
