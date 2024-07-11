import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    return render_template(
        "b8-6.html",
        result=False,
    )


@app.route("/", methods=["POST"])
def output():
    event_name = request.form["event_name"]
    event_date_str = request.form["event_date"]
    event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d")

    today = datetime.datetime.now()
    days_remaining = (event_date - today).days + 1

    return render_template(
        "b8-6.html",
        name=event_name,
        date=event_date.strftime("%Y/%m/%d"),
        remaining=days_remaining,
        result=True,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
