from Resource import algorithm
from Resource.enumerations import AlgorithmResponse
from Resource.objects import Time
from Database import database


class AlgoTester:
    '''
    Test an algorithm on a single price series.
    '''
    balance = 100000
    maxBalance = 100000
    minBalance = 100000
    purchaseValue = 5000

    def __init__(self, algorithm, data, stockName, dates):
        '''
        data - price series
        '''
        self.algo = algorithm
        self.data = data
        self.dates = dates
        self.stockName = stockName
        self.accountDatabase = database.Database("TestDatabaseAccount")
        self.accountDatabase.createTable("Transactions",
                                         ["order", "price", "amount",
                                          "timestamp"])
        self.accountDatabase.createTable("OpenPositions",
                                         ["price", "amount", "opened"])
        self.accountDatabase.createTable("ClosedPositions",
                                         ["openPrice", "closePrice", "amount",
                                          "closed"])

    def updateBalance(self, difference):
        self.balance += difference
        self.maxBalance = self.balance if (self.balance > self.maxBalance) \
            else self.maxBalance
        self.minBalance = self.balance if (self.balance < self.minBalance) \
            else self.minBalance

    def buy(self, timestamp, price, amount):
        print("Buying: " + str(amount) + " $" + str(price) + " @: " +
              str(timestamp))
        self.accountDatabase.insert("Transactions",
                                    ["Buy", price, amount, timestamp])
        row = self.accountDatabase.nextFromTable("OpenPositions")
        if (row is not None):
            oldAmount = int(row["amount"])
            newAmount = oldAmount + amount
            oldPrice = float(row["price"])
            newPrice = (oldPrice * oldAmount + price * amount) / newAmount
            self.accountDatabase.update("OpenPositions", ["amount", "price"],
                                        [newAmount, newPrice], ["amount"],
                                        [oldAmount])
        else:
            self.accountDatabase.insert("OpenPositions",
                                        [price, amount, timestamp])

        self.updateBalance(-1 * price * amount)

    def sell(self, timestamp, price, amount="all"):
        print("Selling: " + str(amount) + " $" + str(price) + " @: " +
              str(timestamp))
        row = self.accountDatabase.nextFromTable("OpenPositions")
        if (row is None):
            return
        openPrice = float(row["price"])
        if (amount == "all"):
            amount = int(row["amount"])
            self.accountDatabase.deleteRows("OpenPositions", ["price"],
                                            [openPrice])
        else:
            openAmount = int(row["amount"])
            self.accountDatabase.update("OpenPositions", ["amount"],
                                        [openAmount-amount], ["amount"],
                                        [openAmount])
        self.accountDatabase.insert("Transactions",
                                    ["Sell", price, amount, timestamp])
        self.accountDatabase.insert("ClosedPositions",
                                    [openPrice, price, amount, timestamp])

        self.updateBalance(amount * price)

    def evaluate(self, chunkSize):
        '''
        make guesses

        chunkSize - minimum amount of data neccessary to evaluate using algo
        '''
        i = 0
        while (i + chunkSize <= len(self.data)):
            chunk = self.data[i:i+chunkSize]
            lastPrice = self.data[i+chunkSize - 1]
            purchaseAmount = int(self.purchaseValue // lastPrice)
            advice = self.algo.advise(chunk)
            if (advice == AlgorithmResponse.Buy):
                self.buy(self.dates[i+chunkSize - 1], lastPrice,
                         purchaseAmount)
            elif (advice == AlgorithmResponse.Sell):
                self.sell(self.dates[i+chunkSize - 1],
                          self.data[i+chunkSize - 1])
            i += chunkSize

        if (i < len(self.data)):
            self.sell(self.dates[len(self.data) - 1], self.data[-1])

        self.report()

    def report(self):
        print("************ Algorithm Analysis Report ************" + '\n' +
              "Starting balance: 100000" + '\n' +
              "Minimum balance: " + str(self.minBalance) + '\n' +
              "Maximum balance: " + str(self.maxBalance) + '\n' +
              "End balance: " + str(self.balance) + '\n' +
              "Net profit ($): " + str(self.balance - 100000) + '\n' +
              "Net profit (%): " + str(self.balance / 1000 - 100) + '\n' +
              '\n' +
              "Number of transactions: " +
              str(self.accountDatabase.numRows("Transactions")))
