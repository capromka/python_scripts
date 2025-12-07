import requests

def get_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    resp = requests.get(url)
    data = resp.json()
    return data["bpi"]["USD"]["rate"]

print("BTC Price (USD):", get_price())
