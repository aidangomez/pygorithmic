import sqlite3

from Questrade import questrade_request
from Resource.enumerations import Interval, RequestType
from Resource.objects import Time, Quote


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

def fetch_market_data(symbol, start_date, end_date=Time.now(),
                      action=lambda x: return):
    batch_start_time = start_date
    batch_end_time = start_date + 1000
    while (batch_end_time < end_date):
        quotes = stock_quotes(symbol, batch_start_time,
                                             batch_end_time)
        action(quotes)
        
        batch_start_time += 1000
        batch_end_time += 1000

    if batch_start_time < end_date:
        quotes = stock_quotes(symbol, batch_start_time,
                                             end_date)
        action(quotes)
