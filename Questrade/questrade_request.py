import requests
import io

from ..Resource.market_exceptions import *


class MarketRequest:
    '''
    Execute questrade api requests using a market data enabled oAuth key.
        Used for: fetching market data
    '''
    def headers(self, key): return {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        token_file = io.open("questrade-tokens/market-tokens.txt")
        if token_file is None:
            raise Exception("Token file note found at:\
                             questrade-tokens/market-tokens.txt")

        self.key = token_file.readline().strip()
        self.refresh_token = token_file.readline().strip()
        self.server = token_file.readline().strip()
        token_file.close()

    def refresh_authentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token",
                         params={"grant_type": "refresh_token",
                                 "refresh_token": self.refresh_token})
        if (check_request(r)):
            token_file = io.open("questrade-tokens/market-tokens.txt",
                                 mode="wt")
            self.key = r.json()["access_token"]
            self.refresh_token = r.json()["refresh_token"]
            self.server = r.json()["api_server"]
            token_file.writelines(
                '\n'.join([self.key, self.refresh_token, self.server]))
            token_file.close()
        return r

    def get(self, service, params=None):
        r = requests.get(self.server + service,
                         headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()

    def post(self, service, params=None):
        r = requests.post(self.server + service,
                          headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.post(self.server + service,
                              headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()

    def delete(self, service, params=None):
        r = requests.delete(self.server + service,
                            headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.delete(self.server + service,
                                headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()


class AccountRequest:
    '''
    Execute questrade api requests using an account orders enabled oAuth key.
        Used for: buy/sell calls, account information
    '''
    def headers(self, key): return {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        token_file = io.open("questrade-tokens/account-tokens.txt")
        if token_file is None:
            raise Exception("Token file note found at:\
                             questrade-tokens/account-tokens.txt")

        self.key = token_file.readline().strip()
        self.refresh_token = token_file.readline().strip()
        self.server = token_file.readline().strip()
        token_file.close()

    def refresh_authentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token",
                         params={"grant_type": "refresh_token",
                                 "refresh_token": self.refresh_token})
        if (check_request(r)):
            token_file = io.open("questrade-tokens/account-tokens.txt",
                                 mode="wt")
            self.key = r.json()["access_token"]
            self.refresh_token = r.json()["refresh_token"]
            self.server = r.json()["api_server"]
            token_file.writelines(
                '\n'.join([self.key, self.refresh_token, self.server]))
            token_file.close()
        return r

    def get(self, service, params=None):
        r = requests.get(self.server + service,
                         headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()

    def post(self, service, params=None):
        r = requests.post(self.server + service,
                          headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.post(self.server + service,
                              headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()

    def delete(self, service, params=None):
        r = requests.delete(self.server + service,
                            headers=self.headers(self.key), params=params)
        try:
            check_request(r)
        except (AccessTokenError, BadRequestError):
            self.refresh_authentication()
            r = requests.delete(self.server + service,
                                headers=self.headers(self.key), params=params)
        except RetryCall:
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return check_request(r).json()
