from dateutil.relativedelta import *


class AlgorithmResponse:
    Buy = "Buy"
    Sell = "Sell"
    Hold = "Hold"


class SortingOrder:
    Ascending = "ASC"
    Descending = "DESC"


class Interval:

    class OneMinute:
        string = "OneMinute"
        delta = relativedelta(minutes=1)

    class TwoMinutes:
        string = "TwoMinutes"
        delta = relativedelta(minutes=2)

    class ThreeMinutes:
        string = "ThreeMinutes"
        delta = relativedelta(minutes=3)

    class FourMinutes:
        string = "FourMinutes"
        delta = relativedelta(minutes=4)

    class FiveMinutes:
        string = "FiveMinutes"
        delta = relativedelta(minutes=5)

    class TenMinutes:
        string = "TenMinutes"
        delta = relativedelta(minutes=10)

    class FifteenMinutes:
        string = "FifteenMinutes"
        delta = relativedelta(minutes=15)

    class TwentyMinutes:
        string = "TwentyMinutes"
        delta = relativedelta(minutes=20)

    class HalfHour:
        string = "HalfHour"
        delta = relativedelta(minutes=30)

    class OneHour:
        string = "OneHour"
        delta = relativedelta(hours=1)

    class TwoHours:
        string = "TwoHours"
        delta = relativedelta(hours=2)

    class FourHours:
        string = "FourHours"
        delta = relativedelta(hours=4)

    class OneDay:
        string = "OneDay"
        delta = relativedelta(days=1)

    class OneWeek:
        string = "OneWeek"
        delta = relativedelta(weeks=1)

    class OneMonth:
        string = "OneMonth"
        delta = relativedelta(months=1)

    class OneYear:
        string = "OneYear"
        delta = relativedelta(years=1)


class OrderType:
    Market = "Market"
    Limit = "Limit"
    Stop = "Stop"
    StopLimit = "StopLimit"
    TrailStopInPercentage = "TrailStopInPercentage"
    TrailStopInDollar = "TrailStopInDollar"
    TrailStopLimitInPercentage = "TrailStopLimitInPercentage"
    TrailStopLimitInDollar = "TrailStopLimitInDollar"
    LimitOnOpen = "LimitOnOpen"
    LimitOnClose = "LimitOnClose"


class RequestType:

    class Market:
        searchSymbol = "v1/symbols/search"

        def getInfo(id): return "v1/symbols/%s" % id

        def getQuotes(id): return "v1/markets/candles/%s" % id

    class Account:
        getAccounts = "v1/accounts"

        def getPositions(id): return "v1/accounts/%s/positions" % id

        def getBalances(id): return "v1/accounts/%s/balances" % id

        def getExecutions(id): return "v1/accounts/%s/executions" % id

        def order(id): return "v1/accounts/%s/orders" % id
