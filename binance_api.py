import requests

def make_request():
    get_result = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return round(float(get_result.json()["price"]), 2)
