from datetime import datetime, timedelta

from flask import Flask, render_template

app = Flask(__name__)


class Event:
    def __init__(self, id, name, date, place):
        self.id = id
        self.name = name
        self.date = date
        self.place = place


@app.template_filter("diff")
def diff_filter(date: datetime):
    diff = date - datetime.now()
    return diff.days


app.jinja_env.filters["diff"] = diff_filter


@app.route("/")
def route():
    events = [
        Event(
            "1",
            "Event 1",
            datetime.fromisoformat("2024-04-11T15:16:00"),
            "Place 1",
        ),
        Event(
            "2",
            "Event 2",
            datetime.fromisoformat("2024-06-05T00:00:00"),
            "Place 2",
        ),
        Event(
            "3",
            "Event 3",
            datetime.fromisoformat("2024-09-27T23:59:59"),
            "Place 3",
        ),
    ]
    return render_template(
        "a3-3.html", title="イベント", events=events, now=datetime.now()
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
