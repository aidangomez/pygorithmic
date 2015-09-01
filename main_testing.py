import Debug.plot_graph
import account_manager
import market_fetcher
import questrade_request
import Resource.enumerations
import Resource.indicators
import Resource.objects

if __name__ == '__main__':
    prices = []
    stockName = "AAPL"
    start = "2013-01-01"
    end = "2014-01-01"
    quotes = market_fetcher.stockQuotes(stockName, start, end, Resource.enumerations.Time.OneDay)

    i=0
    for quote in quotes:
        i = i + 1
        quote = Resource.objects.Quote(quote)
        prices.append(quote.close)
        if (i == 165):
            print(quote.end)

    print(prices)
    Debug.plot_graph.drawLines(Resource.indicators.movingAverageConvergenceDivergence(prices))
