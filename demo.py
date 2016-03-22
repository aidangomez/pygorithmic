from pygorithmic.Database.database import *
from pygorithmic.Database import populate_database

from pygorithmic.Debug.algo_tester import *
from pygorithmic.Debug.plot_graph import *
from pygorithmic.Debug.sample_algo import *

from pygorithmic.Resource.algorithm import *
from pygorithmic.Resource.enumerations import *
from pygorithmic.Resource.indicators import *
from pygorithmic.Resource.objects import *

from pygorithmic.Questrade.account_manager import *
from pygorithmic.Questrade.market_fetcher import *
from pygorithmic.Questrade.questrade_request import *


if __name__ == '__main__':
    # Using AAPL with data from Jan 1, 1990 to today
    stock_name = "AAPL"
    start_date = Time(year=1990, month=1, day=1)

    data = []
    dates = []

    # Create a database and populate it with Apple's trade data
    db = Database("demo")
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
