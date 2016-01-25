from Database.database import *
from Database import populate_database

from Debug.algo_tester import *
from Debug.plot_graph import *
from Debug.sample_algo import *

from Resource.algorithm import *
from Resource.enumerations import *
from Resource.indicators import *
from Resource.objects import *

from Questrade.account_manager import *
from Questrade.market_fetcher import *
from Questrade.questrade_request import *


if __name__ == '__main__':
    # Using AAPL with data from 1990 to today
    stock_name = "NUGT"
    start_date = Time(year=2014, month=1, day=1)

    data = []
    dates = []

    # Create a database and populate it with Apple's trade data
    db = Database("test")
    populate_database.populate(db, stock_name, start_date)

    db.cursor.execute("SELECT * FROM {}".format(stock_name))

    row = db.cursor.fetchone()
    while (row is not None):
        data.append(float(row['close']))
        dates.append(row['timestamp'])
        row = db.cursor.fetchone()

    # algo = TestAlgo(data[:27])
    algo = MACDAlgo(data[:27])
    # algo = RSIAlgo(data[:27])

    tester = AlgoTester(algo, data[27:], stock_name, dates[27:])
    tester.evaluate(1)
