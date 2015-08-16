import requests
import io

from market_exceptions import *


tokenFile = io.open("tokeninfo.txt")
key = tokenFile.readline().strip()
refreshToken = tokenFile.readline().strip()
server = tokenFile.readline().strip()
tokenFile.close()

headers = lambda key: {"Authorization": "Bearer " + key}

services = {"search_symbol":"v1/symbols/search", "stock_info":"v1/symbols/", "get_quotes":"v1/makets/candles/"}

def checkRequest(request):
     code = request.status_code
     if (code == 200):
         return 1
     elif (code == 202):
         return 1
     elif (code == 401):
         raise AccessTokenError("bad access token")
     elif (code == 400):
         raise BadRequestError("bad request")
     elif (code == 404):
         raise InvalidEndpointError("invalid endpoint")
     else:
         print("ERROR: " + str(code))
         print(request.text)
         raise Exception

def refreshAuthentication():
    global key
    global refreshToken
    global server
    r = requests.get("https://login.questrade.com/oauth2/token", params={"grant_type":"refresh_token", "refresh_token":refreshToken})
    if (checkRequest(r)):
        tokenFile = io.open("tokeninfo.txt", mode="wt")
        key = r.json()["access_token"]
        refreshToken = r.json()["refresh_token"]
        server = r.json()["api_server"]
        tokenFile.writelines('\n'.join([key, refreshToken, server]))
        tokenFile.close()
    return r

def send(service, params = None):
    r = requests.get(server + service, headers=headers(key))
    try:
        checkRequest(r)
    except AccessTokenError:
        refreshAuthentication()
        r = requests.get(server + service, headers=headers(key))
    return r


if __name__ == "__main__":
    response = send("v1/accounts")
    print(response.text)
