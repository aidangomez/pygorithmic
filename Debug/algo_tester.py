from Resource import algorithm
from Resource.enumerations import AlgorithmResponse
from Resource.objects import Time
from Database import database


class AlgoTester:
    '''
    Test an algorithm on a single price series.
    '''
    self.balance = 1000
    self.maxBalance = 1000
    self.minBalance = 1000
    self.purchasePrice = 50

    def __init__(self, algorithm, data):
        '''
        data - price series
        '''
        self.algo = algorithm
        self.data = data
        self.accountDatabase = database.Database("TestDatabaseAccount")
        self.accountDatabase.createTable("Transactions",
                                         ["order", "price", "amount",
                                          "timestamp"])
        self.accountDatabase.createTable("OpenPositions",
                                         ["price", "amount", "opened"])
        self.accountDatabase.createTable("ClosedPositions",
                                         ["openPrice", "closePrice", "amount",
                                          "closed"])

    def setParams(self, stockName, startDate):
        '''
        startDate - should be a Resource.objects.Time instance
        '''
        self.stockName = stockName
        self.date = startDate

    def updateBalance(self, difference):
        self.balance += difference
        self.maxBalance = self.balance if (self.balance > self.maxBalance)
        self.minBalance = self.balance if (self.balance < self.minBalance)

    def buy(self, timestamp, price, amount):
        self.accountDatabase.insert("Transactions", ["Buy", price, amount,
                                                     timestamp])
        row = self.accountDatabase.nextFromTable("OpenPositions")
        oldAmount = row["amount"]
        newAmount = oldAmount + amount
        oldPrice = row["price"]
        newPrice = (oldPrice * oldAmount + newPrice * amount) / newAmount
        self.accountDatabase.update("OpenPositions", ["amount", "price"],
                                    [newAmount, newPrice], ["amount"],
                                    [oldAmount])
        updateBalance(price * amount)

    def sell(self, timestamp, price, amount="all"):
        row = self.accountDatabase.nextFromTable("OpenPositions")
        openPrice = row["price"]
        if (amount == "all"):
            amount = row["amount"]
            self.accountDatabase.delete("OpenPositions", ["price"],
                                        [openPrice])
        else:
            openAmount = row["amount"]
            self.accountDatabase.update("OpenPositions", ["amount"],
                                        [openAmount-amount], ["amount"],
                                        [openAmount])
        self.accountDatabase.insert("Transactions",
                                    ["Sell", price, amount, timestamp])
        self.accountDatabase.insert("ClosedPositions",
                                    [openPrice, price, amount, timestamp])
        updateBalance(-1 * amount * price)

    def evaluate(self, chunkSize):
        '''
        make guesses

        chunkSize - minimum amount of data neccessary to evaluate using algo
        '''
        i = 0
        while (i + chunkSize <= len(data)):
            self.date += chunkSize
            chunk = self.data[i:i+chunkSize]
            lastPrice = self.data[i+chunkSize - 1]
            purchaseAmount = self.purchasePrice / lastPrice
            advice = self.algo.advise(chunk)
            if (advice == AlgorithmResponse.Buy):
                self.buy(self.date, lastPrice,
                         purchaseAmount)
            elif (advice == AlgorithmResponse.Sell):
                self.sell(self.date, self.data[i+chunkSize - 1])
            i += chunkSize

    def report(self):
        # TODO: finish
        pass
