from Resource import algorithm
from Resource.enumerations import AlgorithmResponse
from Resource.objects import Time
from Database.temporary_database import TemporaryDatabase


class AlgoTester:
    '''
    Test an algorithm on a single price series.
    '''
    balance = 100000
    max_balance = 100000
    min_balance = 100000
    purchase_value = 5000

    def __init__(self, algorithm, data, stock_name, dates):
        '''
        data - price series
        '''
        self.algo = algorithm
        self.data = data
        self.dates = dates
        self.stock_name = stock_name
        self.account_database = TemporaryDatabase("TestDatabaseAccount")
        self.account_database.create_table("Transactions",
                                           ["order", "price", "amount",
                                            "timestamp"])
        self.account_database.create_table("OpenPositions",
                                           ["price", "amount", "opened"])
        self.account_database.create_table("ClosedPositions",
                                           ["openPrice", "closePrice",
                                            "amount", "closed"])

    def update_balance(self, difference):
        self.balance += difference
        self.max_balance = self.balance if (self.balance > self.max_balance) \
            else self.max_balance
        self.min_balance = self.balance if (self.balance < self.min_balance) \
            else self.min_balance

    def buy(self, timestamp, price, amount):
        print("Buying: " + str(amount) + " $" + str(price) + " @: " +
              str(timestamp))
        self.account_database.insert("Transactions",
                                     ["Buy", price, amount, timestamp])
        row = self.account_database.next_from_table("OpenPositions")
        if (row is not None):
            old_amount = int(row["amount"])
            new_amount = old_amount + amount
            old_price = float(row["price"])
            new_price = (old_price * old_amount + price * amount) / new_amount
            self.account_database.update("OpenPositions", ["amount", "price"],
                                         [new_amount, new_price], ["amount"],
                                         [old_amount])
        else:
            self.account_database.insert("OpenPositions",
                                         [price, amount, timestamp])

        self.update_balance(-1 * price * amount)

    def sell(self, timestamp, price, amount="all"):
        print("Selling: " + str(amount) + " $" + str(price) + " @: " +
              str(timestamp))
        row = self.account_database.next_from_table("OpenPositions")
        if (row is None):
            return
        open_price = float(row["price"])
        if (amount == "all"):
            amount = int(row["amount"])
            self.account_database.delete_rows("OpenPositions", ["price"],
                                              [open_price])
        else:
            open_amount = int(row["amount"])
            self.account_database.update("OpenPositions", ["amount"],
                                         [open_amount - amount], ["amount"],
                                         [open_amount])
        self.account_database.insert("Transactions",
                                     ["Sell", price, amount, timestamp])
        self.account_database.insert("ClosedPositions",
                                     [open_price, price, amount, timestamp])

        self.update_balance(amount * price)

    def evaluate(self, chunk_size):
        '''
        make guesses

        chunk_size - minimum amount of data neccessary to evaluate using algo
        '''
        i = 0
        while (i + chunk_size <= len(self.data)):
            chunk = self.data[i:i + chunk_size]
            last_price = self.data[i + chunk_size - 1]
            purchase_amount = int(self.purchase_value // last_price)
            advice = self.algo.advise(chunk)
            if (advice == AlgorithmResponse.buy):
                self.buy(self.dates[i + chunk_size - 1], last_price,
                         purchase_amount)
            elif (advice == AlgorithmResponse.sell):
                self.sell(self.dates[i + chunk_size - 1],
                          self.data[i + chunk_size - 1])
            i += chunk_size

        self.sell(self.dates[len(self.data) - 1], self.data[-1])

        self.report()

    def report(self):
        print("************ Algorithm Analysis Report ************" + '\n' +
              "Starting balance: 100000" + '\n' +
              "Minimum balance: " + str(self.min_balance) + '\n' +
              "Maximum balance: " + str(self.max_balance) + '\n' +
              "End balance: " + str(self.balance) + '\n' +
              "Net profit ($): " + str(self.balance - 100000) + '\n' +
              "Net profit (%): " + str(self.balance / 1000 - 100) + '\n' +
              '\n' +
              "Number of transactions: " +
              str(self.account_database.row_count("Transactions")))
