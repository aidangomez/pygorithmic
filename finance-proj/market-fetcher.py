import requests
import io

tokenFile = io.open("tokeninfo.txt")
key = tokenFile.readline().strip()
refreshToken = tokenFile.readline().strip()

server = "https://api01.iq.questrade.com/v1/"

services = {"search_symbol":"symbols/search", "stock_info":"symbols/", "get_quotes":"makets/candles/"}

def refresh_authentication():
    r = requests.get("https://login.questrade.com/oauth2/token", params={"grant_type":"refresh_token", "refresh_token":refreshToken})
    print("REFRESH " + r.text)
    key = r.json()["access_token"]
    refresh_token = r.json()["refresh_token"]
    # tokenFile.writelines([key, refresh_token])
    return r

def send(service, params = None):
    headers = {"Authorization": "Bearer " + key}
    r = requests.get(server + service, headers=headers)
    print(key)
    print(refreshToken)
    print("RESPONSE " + r.text)
    print("REFRESH " + refresh_authentication().text)
    r = requests.get(server + service, headers=headers, params=params)
    return r


# JP4ADoI9Ma8l6QGEDAfb3tRrHwfnU2qQ0
# {"access_token":"JP4ADoI9Ma8l6QGEDAfb3tRrHwfnU2qQ0","api_server":"https:\/\/api01.iq.questrade.com\/","expires_in":1800,"refresh_token":"TK_k5XiWnBe9dSKO_asCEEHExgA2teHe0","token_type":"Bearer"}

if __name__ == "__main__":
    # response = a.refresh_authentication()
    # print(response.text)
    response = send("accounts")
    print("RESPONSE " + response.text)
