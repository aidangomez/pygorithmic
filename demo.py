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
from market_fetcher import *
from questrade_request import *


if __name__ == '__main__':
    stockName = "AAPL"
    startDate = Time(1990, 1, 1)

    data = []

    db = database.Database("test")
    db.cursor.execute("SELECT * FROM {}".format(stockName))
    row = db.cursor.fetchone()
    while (row is not None):
        data += row['close']
        row = db.cursor.fetchone()

    tester = AlgoTester(, data)
