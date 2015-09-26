import requests
import io

from Resource.market_exceptions import *


class MarketRequest:
    '''
    Execute questrade api requests using a market data enabled oAuth key.
        Used for: fetching market data
    '''
    def headers(self, key): return {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        tokenFile = io.open("questrade-tokens/market-tokens.txt")
        if tokenFile is None:
            raise Exception("Token file note found at: questrade-tokens/market-tokens.txt")

        self.key = tokenFile.readline().strip()
        self.refreshToken = tokenFile.readline().strip()
        self.server = tokenFile.readline().strip()
        tokenFile.close()

    def refreshAuthentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token",
                         params={"grant_type": "refresh_token",
                                 "refresh_token": self.refreshToken})
        if (checkRequest(r)):
            tokenFile = io.open("questrade-tokens/market-tokens.txt", mode="wt")
            self.key = r.json()["access_token"]
            self.refreshToken = r.json()["refresh_token"]
            self.server = r.json()["api_server"]
            tokenFile.writelines(
                '\n'.join([self.key, self.refreshToken, self.server]))
            tokenFile.close()
        return r

    def get(self, service, params=None):
        r = requests.get(self.server + service,
                         headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return checkRequest(r).json()

    def post(self, service, params=None):
        r = requests.post(self.server + service,
                          headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.post(self.server + service,
                              headers=self.headers(self.key), params=params)
        return checkRequest(r).json()

    def delete(self, service, params=None):
        r = requests.delete(self.server + service,
                            headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.delete(self.server + service,
                                headers=self.headers(self.key), params=params)
        return checkRequest(r).json()


class AccountRequest:
    '''
    Execute questrade api requests using an account orders enabled oAuth key.
        Used for: buy/sell calls, account information
    '''
    def headers(self, key): return {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        tokenFile = io.open("questrade-tokens/account-tokens.txt")
        if tokenFile is None:
            raise Exception("Token file note found at: questrade-tokens/account-tokens.txt")

        self.key = tokenFile.readline().strip()
        self.refreshToken = tokenFile.readline().strip()
        self.server = tokenFile.readline().strip()
        tokenFile.close()

    def refreshAuthentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token",
                         params={"grant_type": "refresh_token",
                                 "refresh_token": self.refreshToken})
        if (checkRequest(r)):
            tokenFile = io.open("questrade-tokens/account-tokens.txt", mode="wt")
            self.key = r.json()["access_token"]
            self.refreshToken = r.json()["refresh_token"]
            self.server = r.json()["api_server"]
            tokenFile.writelines(
                '\n'.join([self.key, self.refreshToken, self.server]))
            tokenFile.close()
        return r

    def get(self, service, params=None):
        r = requests.get(self.server + service,
                         headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.get(self.server + service,
                             headers=self.headers(self.key), params=params)
        return checkRequest(r).json()

    def post(self, service, params=None):
        r = requests.post(self.server + service,
                          headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.post(self.server + service,
                              headers=self.headers(self.key), params=params)
        return checkRequest(r).json()

    def delete(self, service, params=None):
        r = requests.delete(self.server + service,
                            headers=self.headers(self.key), params=params)
        try:
            checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.delete(self.server + service,
                                headers=self.headers(self.key), params=params)
        return checkRequest(r).json()
