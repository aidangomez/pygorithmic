import requests
import io

from market_exceptions import *

class MarketRequest:
    headers = lambda self, key: {"Authorization": "Bearer " + self.key}

    def __init__(self):
        # read in token information
        tokenFile = io.open("tokeninfo.txt")
        self.key = tokenFile.readline().strip()
        self.refreshToken = tokenFile.readline().strip()
        self.server = tokenFile.readline().strip()
        tokenFile.close()

    def checkRequest(self, request):
         code = request.status_code
         if (code == 200):
             return 1
         elif (code == 202):
             return 1
         elif (code == 401):
             raise AccessTokenError("Bad access token.")
         elif (code == 400):
             raise BadRequestError("Bad request.")
         elif (code == 404):
             raise InvalidEndpointError("Invalid endpoint: " + request.url)
         elif (code == 429):
             raise LimitExceededError("Too many requests. Reset in: " + str(request.headers["X-RateLimit-Reset"]))
         else:
             print("ERROR: " + str(code))
             print(request.text)
             raise Exception

    def refreshAuthentication(self):
        r = requests.get("https://login.questrade.com/oauth2/token", params={"grant_type":"refresh_token", "refresh_token":self.refreshToken})
        if (self.checkRequest(r)):
            tokenFile = io.open("tokeninfo.txt", mode="wt")
            self.key = r.json()["access_token"]
            self.refreshToken = r.json()["refresh_token"]
            self.server = r.json()["api_server"]
            tokenFile.writelines('\n'.join([self.key, self.refreshToken, self.server]))
            tokenFile.close()
        return r

    def send(self, service, params = None):
        r = requests.get(self.server + service, headers=self.headers(self.key), params=params)
        try:
            self.checkRequest(r)
        except (AccessTokenError, BadRequestError):
            self.refreshAuthentication()
            r = requests.get(self.server + service, headers=self.headers(self.key), params=params)
        return r.json()
