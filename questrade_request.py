import requests
import io

from Resource.market_exceptions import *


class MarketRequest:
    headers = lambda self, key: {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        tokenFile = io.open("Tokens/mrkt_token.txt")
        self.key = tokenFile.readline().strip()
        self.refreshToken = tokenFile.readline().strip()
        self.server = tokenFile.readline().strip()
        tokenFile.close()

    def refreshAuthentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token", params={
                         "grant_type": "refresh_token", "refresh_token": self.refreshToken})
        if (checkRequest(r)):
            tokenFile = io.open("Tokens/mrkt_token.txt", mode="wt")
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
    headers = lambda self, key: {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        tokenFile = io.open("Tokens/acnt_token.txt")
        self.key = tokenFile.readline().strip()
        self.refreshToken = tokenFile.readline().strip()
        self.server = tokenFile.readline().strip()
        tokenFile.close()

    def refreshAuthentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token", params={
                         "grant_type": "refresh_token", "refresh_token": self.refreshToken})
        if (checkRequest(r)):
            tokenFile = io.open("Tokens/acnt_token.txt", mode="wt")
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
