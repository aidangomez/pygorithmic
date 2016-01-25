from Questrade import questrade_request
from Resource.enumerations import RequestType


class Account:
    def __init__(self, account_type, number, status):
        self.type = account_type
        self.number = number
        self.status = status

    def buy(symbol_id, quantity, limit, stop, order_type, AON=False,
            iceberg=None):
        '''
        iceberg - will repeatedly place orders of size iceberg until the full
                    order has been filled
        '''
        params = {
                  "symbolId": symbol_id,
                  "quantity": quantity,
                  "iceberg": iceberg,
                  "limitPrice": limit,
                  "stopPrice": stop,
                  "isAllOrNone": AON,
                  "orderType": order_type,
                  "action": "Buy"
        }
        r = questrade_request.AccountRequest.post(RequestType.Account
                                                  .order(self.number),
                                                  params=params)
        return r.json()["filledQuantity"]

    def sell(symbol_id, quantity, limit, stop, order_type, AON=False,
             iceberg=None):
        '''
        iceberg - will repeatedly place orders of size iceberg until the full
                    order has been filled
        '''
        params = {
                  "symbolId": symbol_id,
                  "quantity": quantity,
                  "iceberg": iceberg,
                  "limitPrice": limit,
                  "stopPrice": stop,
                  "isAllOrNone": AON,
                  "orderType": order_type,
                  "action": "Sell"
        }
        r = questrade_request.AccountRequest.post(RequestType.Account
                                                  .order(self.number),
                                                  params=params)
        return r.json()["filledQuantity"]
