import sqlite3
from datetime import datetime

from flask import Flask, g, render_template

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("events.db")
    return g.db


def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/", methods=["GET"])
def database():
    db = get_db()
    query = db.execute("SELECT * FROM events")
    events = query.fetchall()
    events = list(events)

    for index, event in enumerate(events):
        event = list(event)
        event[2] = datetime.strptime(event[2], "%Y-%m-%d").date()
        events[index] = event

    close_db()

    schema = ["ID", "Name", "Date", "Place"]
    return render_template(
        "a5-2.html",
        title="Events",
        schema=schema,
        events=events,
        now=datetime.now().date(),
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
