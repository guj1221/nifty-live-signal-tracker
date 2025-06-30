import requests
from datetime import datetime

def get_nifty_price(token):
    url = "https://api.groww.in/v1/live-data/ltp"
    params = {"exchange": "NSE", "segment": "CASH", "trading_symbol": "NIFTY"}
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(url, params=params, headers=headers)
    return float(res.json()["payload"]["last_price"]), datetime.now().strftime("%H:%M:%S")
