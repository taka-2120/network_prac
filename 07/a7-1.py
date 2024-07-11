import sqlite3
from datetime import datetime

from flask import Flask, g, render_template, request

app = Flask(__name__)
SCHEMA = ["ID", "Name", "Date", "Place"]


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

    return render_template(
        "a7-1.html",
        message="",
        schema=SCHEMA,
        events=events,
        now=datetime.now().date(),
    )


@app.route("/", methods=["POST"])
def post():
    action = request.form["action"]
    if action == "Insert":
        return insert()
    if action == "Delete":
        return delete()
    if action == "Search":
        return search()
    return "Invalid action"


def get_events():
    db = get_db()
    query = db.execute("SELECT * FROM events")
    events = query.fetchall()
    events = list(events)

    for index, event in enumerate(events):
        event = list(event)
        event[2] = datetime.strptime(event[2], "%Y-%m-%d").date()
        events[index] = event

    close_db()
    return events


def insert():
    name = request.form["name"]
    date = request.form["date"]
    place = request.form["place"]

    if not name or not date or not place:
        return render_template(
            "a7-1.html",
            message="Invalid input. Please fill all add fields.",
            schema=SCHEMA,
            events=get_events(),
            now=datetime.now().date(),
        )

    db = get_db()

    query = db.execute(
        f"INSERT INTO events(name, date, place) VALUES('{name}','{date}','{place}')"
    )
    db.commit()
    query = db.execute("SELECT * FROM events")
    events = query.fetchall()
    events = list(events)

    for index, event in enumerate(events):
        event = list(event)
        event[2] = datetime.strptime(event[2], "%Y-%m-%d").date()
        events[index] = event

    close_db()

    return render_template(
        "a7-1.html",
        message="Event has successfully added",
        schema=SCHEMA,
        events=events,
        now=datetime.now().date(),
    )


def delete():
    event_id = request.form["id"]

    if not event_id:
        return render_template(
            "a7-1.html",
            message="Invalid input. Please fill id field in delete section.",
            schema=SCHEMA,
            events=get_events(),
            now=datetime.now().date(),
        )

    db = get_db()

    query = db.execute(f"DELETE FROM events WHERE id = {event_id}")
    db.commit()
    query = db.execute("SELECT * FROM events")
    events = query.fetchall()
    events = list(events)

    for index, event in enumerate(events):
        event = list(event)
        event[2] = datetime.strptime(event[2], "%Y-%m-%d").date()
        events[index] = event

    close_db()

    return render_template(
        "a7-1.html",
        message="Event has successfully deleted.",
        schema=SCHEMA,
        events=events,
        now=datetime.now().date(),
    )


def search():
    name = request.form["search_name"]
    year = request.form["search_year"]
    month = request.form["search_month"]
    day = request.form["search_day"]
    place = request.form["search_place"]

    db = get_db()

    search_queries = []

    if name:
        search_queries.append(f" name LIKE '%{name}%'")
    if year:
        search_queries.append(f" date LIKE '%{year}%'")
    if month:
        search_queries.append(f" date LIKE '%-{month}-%'")
    if day:
        search_queries.append(f" date LIKE '%-{day}-%'")
    if place:
        search_queries.append(f" place LIKE '%{place}%'")

    query_str = "SELECT * FROM events"
    for index, search_query in enumerate(search_queries):
        if index != 0:
            query_str += " AND"
        if index == 0:
            query_str += " WHERE"
        query_str += search_query

    query = db.execute(query_str)
    events = query.fetchall()
    events = list(events)

    for index, event in enumerate(events):
        event = list(event)
        event[2] = datetime.strptime(event[2], "%Y-%m-%d").date()
        events[index] = event

    close_db()

    return render_template(
        "a7-1.html",
        message="",
        schema=SCHEMA,
        events=events,
        now=datetime.now().date(),
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5600)
