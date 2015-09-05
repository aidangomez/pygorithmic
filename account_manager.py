import questrade_request
from Resource.enumerations import RequestType


class Account:
    def __init__(self, acntType, number, status):
        self.type = acntType
        self.number = number
        self.status = status

    def buy(symbolId, quantity, limit, stop, orderType, AON=False,
            iceberg=None):
        '''
        iceberg - will repeatedly place orders of size iceberg until the full
                    order has been filled
        '''
        params = {
                  "symbolId": symbolId,
                  "quantity": quantity,
                  "iceberg": iceberg,
                  "limitPrice": limit,
                  "stopPrice": stop,
                  "isAllOrNone": AON,
                  "orderType": orderType,
                  "action": "Buy"
        }
        r = questrade_request.AccountRequest.post(RequestType.Account
                                                  .order(self.number),
                                                  params=params)
        return r.json()["filledQuantity"]

    def sell(symbolId, quantity, limit, stop, orderType, AON=False,
             iceberg=None):
        '''
        iceberg - will repeatedly place orders of size iceberg until the full
                    order has been filled
        '''
        params = {
                  "symbolId": symbolId,
                  "quantity": quantity,
                  "iceberg": iceberg,
                  "limitPrice": limit,
                  "stopPrice": stop,
                  "isAllOrNone": AON,
                  "orderType": orderType,
                  "action": "Sell"
        }
        r = questrade_request.AccountRequest.post(RequestType.Account
                                                  .order(self.number),
                                                  params=params)
        return r.json()["filledQuantity"]
