import Debug.plot_graph
import Debug.algo_tester

import Resource.enumerations
import Resource.indicators
import Resource.objects
import Resource.algorithm

import account_manager
import market_fetcher
import questrade_request


if __name__ == '__main__':
    prices = []
    stockName = "AAPL"
    start = "2015-09-01"
    end = "2015-09-02"
    timeFrame = Resource.enumerations.Interval.OneMinute.string

    quotes = market_fetcher.stockQuotes(stockName, start, end, timeFrame)

    i = 0
    for quote in quotes:
        i = i + 1
        quote = Resource.objects.Quote(quote)
        prices.append(quote.close)
        if (i == 165):
            print(quote.end)

    print(prices)
    Debug.plot_graph.drawLines(Resource.indicators
                               .movingAverageConvergenceDivergence(prices))
