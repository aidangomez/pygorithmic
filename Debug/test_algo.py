from ..Resource import algorithm
from ..Resource.objects import Time
from ..Database import database

class AlgoTester:
    '''
    Test an algorithm on a single price series.
    '''
    def __init__(self, algorithm, data):
        '''
        data - price series
        '''
        self.algo = algorithm
        self.data = data
        self.accountDatabase = database.Database("TestDatabaseAccount")
        self.accountDatabase.createTable("Transactions", ["order", "price", "amount", "timestamp"])
        self.accountDatabase.createTable("OpenPositions", ["price", "amount", "opened"])
        self.accountDatabase.createTable("ClosedPositions", ["openPrice", "closePrice", "amount", "closed"])

    def setParams(self, stockName, startDate):
        self.stockName = stockName
        self.startDate = startDate

    def genTimestamp(self, i):
        return Time()
        # TODO: complete this function when Time class is completed

    def buy(timestamp, price, amount):
        self.accountDatabase.insert("Transactions", ["Buy", price, amount, timestamp])
        self.accountDatabase.insert("OpenPositions", [price, amount, timestamp])
        # TODO: update amount and price for buy row

    def sell(timestamp, price, amount="all"):
        if (amount == "all"):
            row = self.accountDatabase.nextFromTable("OpenPositions")
            self.accountDatabase.delete("OpenPositions", ["price"], [row["price"]])
            openPrice = row["price"]
            amount = row["amount"]
            self.accountDatabase.insert("Transactions", ["Sell", price, amount, timestamp])
            self.accountDatabase.insert("ClosedPositions", [openPrice, price, amount, timestamp])
        else:
            row = self.accountDatabase.nextFromTable("OpenPositions")
            openPrice = row["price"]
            openAmount = row["amount"]
            self.accountDatabase.update("OpenPositions", ["amount"], [openAmount-amount], ["amount"], [openAmount])
            self.accountDatabase.insert("Transactions", ["Sell", price, amount, timestamp])
            self.accountDatabase.insert("ClosedPositions", [openPrice, price, amount, timestamp])

    def evaluate(self, chunkSize):
        '''
        make guesses

        chunkSize - minimum amount of data neccessary to evaluate using algo
        '''
        i = 0
        while (i + chunkSize <= len(data)):
            chunk = self.data[i:i+chunkSize]
            advice = self.algo.advise(chunk)
            if (advice == "Buy"):
                self.buy()
            elif (advice == "Sell"):
                self.sell()
            i += chunkSize
