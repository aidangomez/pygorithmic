import requests
import json

key = "iL5elbEixTmvV9RXgQHgNphPDwA8E2Wu0"
refresh_token = "F22CT3CDmmmcQ-WVAGImykrKogLEaU370"
server = "https://api01.iq.questrade.com/"

def refresh_authentication():
    r = requests.get("https://login.questrade.com/oauth2/token", params={"grant_type":"refresh_token", "refresh_token":refresh_token})
    key = r.json()["access_token"]
    refresh_token = r.json()["refresh_token"]
    return r

def send(service):
    headers = {"Authorization": "Bearer " + key}
    r = requests.get(server + service, headers=headers)
    return r


# JP4ADoI9Ma8l6QGEDAfb3tRrHwfnU2qQ0
# {"access_token":"JP4ADoI9Ma8l6QGEDAfb3tRrHwfnU2qQ0","api_server":"https:\/\/api01.iq.questrade.com\/","expires_in":1800,"refresh_token":"TK_k5XiWnBe9dSKO_asCEEHExgA2teHe0","token_type":"Bearer"}

if __name__ == "__main__":
    # response = a.refresh_authentication()
    # print(response.text)
    response = send("v1/accounts")
    print(response.text)
