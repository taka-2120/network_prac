from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    prev_id = request.cookies.get("prev_id")
    if prev_id is None:
        prev_id = ""
    return render_template("a6-4in.html", title="Event form", prev_id=prev_id)


@app.route("/", methods=["POST"])
def output():
    event_id = request.form["event_id"]
    template = ""

    if event_id == "1":
        template = event1()
    elif event_id == "2":
        template = event2()
    elif event_id == "3":
        template = event3()
    else:
        template = render_template(
            "a6-4out.html", title="Event form", message="Invalid ID"
        )

    response = make_response(template)
    response.set_cookie("prev_id", event_id)

    return response


def event1():
    return render_template(
        "a4-1out.html",
        title="イベント1",
        id=1,
        name="予定1",
        date="2024/04/01",
        place="場所1",
        future=False,
    )


def event2():
    return render_template(
        "a4-1out.html",
        title="イベント2",
        id=2,
        name="予定2",
        date="2024/04/02",
        place="場所2",
        future=False,
    )


def event3():
    return render_template(
        "a4-1out.html",
        title="イベント3",
        id=3,
        name="予定3",
        date="2024/09/30",
        place="場所3",
        future=True,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
