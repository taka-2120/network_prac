from flask import Flask, render_template

app = Flask(__name__)


@app.route("/id1")
def event1():
    return render_template(
        "a2-3.html",
        title="イベント1",
        id=1,
        name="予定1",
        date="2024/04/01",
        place="場所1",
        future=False,
    )


@app.route("/id2")
def event2():
    return render_template(
        "a2-3.html",
        title="イベント2",
        id=2,
        name="予定2",
        date="2024/04/02",
        place="場所2",
        future=False,
    )


@app.route("/id3")
def event3():
    return render_template(
        "a2-3.html",
        title="イベント3",
        id=3,
        name="予定3",
        date="2024/09/30",
        place="場所3",
        future=True,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
