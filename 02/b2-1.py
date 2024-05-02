import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    r = requests.get("https://latest.currency-api.pages.dev/v1/currencies.json")
    currencies = r.json()
    keys = list(currencies.keys())[7:]
    r = requests.get("https://latest.currency-api.pages.dev/v1/currencies/usd.json")
    base_usd = r.json()

    jpy = base_usd["usd"]["jpy"]
    return render_template(
        "b2-1in.html",
        keys=keys,
        jpy=round(jpy, 2),
    )


@app.route("/result", methods=["POST"])
def output():
    amount = request.form["amount"]
    from_currency = request.form["from_currency"].lower()
    to_currency = request.form["to_currency"].lower()

    r = requests.get(
        "https://latest.currency-api.pages.dev/v1/currencies/{}.json".format(
            from_currency
        )
    )
    json = r.json()
    value = json[from_currency][to_currency]

    result = float(amount) * float(value)
    result = round(result, 2)
    return render_template(
        "b2-1out.html",
        from_currency=from_currency,
        from_amount=amount,
        to_currency=to_currency,
        result=result,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
