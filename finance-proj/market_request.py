import requests
import market-fetcher

def stockQuote(symbol, start_date, end_date):
    stockList = send(services["search_symbol"], params={"prefix":symbol})
    stockId = stockList[0]["symbolId"]

    startDate = start_date + "T00:00:00-05:00"
    endDate = end_date + "T00:00:00-05:00"

    return send(services["get_quotes"], params={"id":stockId, "startTime":startDate, "endTime":endDate, "interval":"FiveMinutes"})

if __name__ == "__main__":
    # response = a.refresh_authentication()
    # print(response.text)
    response = send("accounts")
    print(response.text)
