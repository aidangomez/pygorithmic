from dateutil.relativedelta import *


class AlgorithmResponse:
    buy = "Buy"
    sell = "Sell"
    hold = "Hold"


class SortingOrder:
    ascending = "ASC"
    descending = "DESC"


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
    market = "Market"
    limit = "Limit"
    stop = "Stop"
    stop_limit = "StopLimit"
    trail_stop_in_percentage = "TrailStopInPercentage"
    trail_stop_in_dollar = "TrailStopInDollar"
    trail_stop_limit_in_percentage = "TrailStopLimitInPercentage"
    trail_stop_limit_in_dollar = "TrailStopLimitInDollar"
    limit_on_open = "LimitOnOpen"
    limit_on_close = "LimitOnClose"


class RequestType:

    class Market:
        search_symbol = "v1/symbols/search"

        @staticmethod
        def get_info(id): return "v1/symbols/%s" % id

        @staticmethod
        def get_quotes(id): return "v1/markets/candles/%s" % id

    class Account:
        get_accounts = "v1/accounts"

        @staticmethod
        def get_positions(id): return "v1/accounts/%s/positions" % id

        @staticmethod
        def get_balances(id): return "v1/accounts/%s/balances" % id

        @staticmethod
        def get_executions(id): return "v1/accounts/%s/executions" % id

        @staticmethod
        def order(id): return "v1/accounts/%s/orders" % id
