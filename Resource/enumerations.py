class Time:
    OneMinute = "OneMinute"
    TwoMinutes = "TwoMinutes"
    ThreeMinutes = "ThreeMinutes"
    FourMinutes = "FourMinutes"
    FiveMinutes = "FiveMinutes"
    TenMinutes = "TenMinutes"
    FifteenMinutes = "FifteenMinutes"
    TwentyMinutes = "TwentyMinutes"
    HalfHour = "HalfHour"
    OneHour = "OneHour"
    TwoHours = "TwoHours"
    FourHours = "FourHours"
    OneDay = "OneDay"
    OneWeek = "OneWeek"
    OneMonth = "OneMonth"
    OneYear = "OneYear"

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
        getInfo = lambda id: "v1/symbols/%s" % id
        getQuotes = lambda id: "v1/markets/candles/%s" % id
    class Account:
        getAccounts = "v1/accounts"
        getPositions = lambda id: "v1/accounts/%s/positions" % id
        getBalances = lambda id: "v1/accounts/%s/balances" % id
        getExecutions = lambda id: "v1/accounts/%s/executions" % id
        order = lambda id: "v1/accounts/%s/orders" % id
