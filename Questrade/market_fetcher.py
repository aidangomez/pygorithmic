import sqlite3

from Questrade import questrade_request
from Resource.enumerations import Interval, RequestType
from Resource.objects import Quote


def stock_quotes(symbol, start_date, end_date):
    request = questrade_request.MarketRequest()
    stock_list = request.get(RequestType.Market.search_symbol,
                             params={"prefix": symbol})
    stock_id = stock_list["symbols"][0]["symbolId"]
    return request.get(RequestType.Market.get_quotes(stock_id),
                       params={"startTime": str(start_date),
                               "endTime": str(end_date),
                               "interval": start_date.interval.string
                               })["candles"]
