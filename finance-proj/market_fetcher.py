import market_request
from Resource.enumerations import Time, RequestType

def stockQuote(symbol, startDate, endDate, timeFrame):
    """
    dates povided in string as "year-month-day"
    """
    request = market_request.MarketRequest()
    stockList = request.send(RequestType.searchSymbol, params={"prefix":symbol})
    stockId = stockList["symbols"][0]["symbolId"]

    startDate = startDate + "T00:00:00-05:00"
    endDate = endDate + "T00:00:00-05:00"

    return request.send(RequestType.getQuotes + str(stockId), params={"startTime":startDate, "endTime":endDate, "interval":timeFrame})
