from datetime import date, datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    with open("a4-3.txt", encoding="utf-8") as file:
        events = []
        for text in file:
            event = text.replace("\n", "").split(",")
            print(event[0])
            event[0] = datetime.strptime(event[0], "%Y-%m-%d").date()
            events.append(event)
        schema = ["Date", "Event"]

    return render_template("a4-3.html", schema=schema, events=events, now=date.today())


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
