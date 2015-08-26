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


class RequestType:
    class Market:
        searchSymbol = "v1/symbols/search"
        getInfo = "v1/symbols/"
        getQuotes = "v1/markets/candles/"
    class Account:
        getAccounts = "v1/accounts"
        getPositions = lambda id: "v1/accounts/%s/positions" % id
        getBalances = lambda id: "v1/accounts/%s/balances" % id
        getExecutions = lambda id: "v1/accounts/%s/executions" % id
        order = lambda id: "v1/accounts/%s/orders" % id
