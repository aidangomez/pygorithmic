from Database.database import *
from Database import populate_database

from Debug.algo_tester import *
from Debug.plot_graph import *
from Debug.sample_algo import *

from Resource.algorithm import *
from Resource.enumerations import *
from Resource.indicators import *
from Resource.objects import *

from account_manager import *
from Questrade.market_fetcher import *
from Questrade.questrade_request import *


if __name__ == '__main__':
    # Using AAPL with data from 1990 to today
    stockName = "AAPL"
    startDate = Time(year=1990, month=1, day=1)

    # Use a sample algorithm
    algo = SampleAlgo()

    data = []
    dates = []

    # Create a database and populate it with Apple's trade data
    db = database.Database("test")
    populate_database.populate(db, stockName, startDate)
    
    db.cursor.execute("SELECT * FROM {}".format(stockName))

    row = db.cursor.fetchone()
    while (row is not None):
        data.append(float(row['close']))
        dates.append(row['timestamp'])
        row = db.cursor.fetchone()

    tester = AlgoTester(algo, data, stockName, dates)
    tester.evaluate(5)
