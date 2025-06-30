from flask import Flask, render_template
from market import get_nifty_price
from signal_engine import decide_signal
import json

app = Flask(__name__)
with open("config.json") as f:
    cfg = json.load(f)

prev_price = None

@app.route("/")
def index():
    global prev_price
    price, now = get_nifty_price(cfg["access_token"])
    if prev_price is None:
        prev_price = price

    signal, target = decide_signal(price, prev_price, cfg["target_points"])
    stop = target - cfg["stop_loss_points"] if target else None
    prev_price = price

    return render_template("index.html", price=price, time=now, signal=signal, target=target, stop=stop)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
