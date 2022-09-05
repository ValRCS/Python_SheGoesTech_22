import json
import requests


# Getting crypto prices

def get_crypto_prices(url="https://api2.binance.com/api/v3/ticker/24hr"):
    response = requests.get(url)  # so we made a HTTP GET request here just like a browser would
    prices = dict()  # dict with trading pair prices

    print(response.status_code)  # Response Code 200 is good! 404 not good :)
    data_from_json = response.json()

    for i in range(len(data_from_json)):  # we getting only last prices
        symbol = data_from_json[i].get("symbol")
        last_price = data_from_json[i].get("lastPrice")
        prices[i] = symbol, last_price

    with open("data_from_url.json", mode="w") as write_file:  # saving data to json
        json.dump(prices, write_file, indent=4)

    return prices


print(get_crypto_prices())
