import sqlite3

from Questrade import questrade_request
from Resource.enumerations import Interval, RequestType
from Resource.objects import Quote


def stockQuotes(symbol, startDate, endDate):
    request = questrade_request.MarketRequest()
    stockList = request.get(RequestType.Market.searchSymbol,
                            params={"prefix": symbol})
    stockId = stockList["symbols"][0]["symbolId"]

    return request.get(RequestType.Market.getQuotes(stockId),
                       params={"startTime": str(startDate),
                               "endTime": str(endDate),
                               "interval": startDate.interval.string
                               })["candles"]
