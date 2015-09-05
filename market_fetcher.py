import sqlite3

import questrade_request
from Resource.enumerations import Interval, RequestType
from Resource.objects import Quote


def stockQuotes(symbol, startDate, endDate, interval):
    """
    interval is an Resource.enumerations.Interval

    """
    request = questrade_request.MarketRequest()
    stockList = request.get(RequestType.Market.searchSymbol,
                            params={"prefix": symbol})
    stockId = stockList["symbols"][0]["symbolId"]

    return request.get(RequestType.Market.getQuotes(stockId),
                       params={"startTime": startDate,
                               "endTime": endDate,
                               "interval": interval.string})["candles"]
