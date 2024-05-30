from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    prevId = request.cookies.get("prev_id")
    if prevId is None:
        prevId = ""
    return render_template("a4-1in.html", title="Event form", prevId=prevId)


@app.route("/", methods=["POST"])
def output():
    eventId = request.form["eventId"]
    template = ""

    if eventId == "1":
        template = event1()
    elif eventId == "2":
        template = event2()
    elif eventId == "3":
        template = event3()
    else:
        template = render_template(
            "a4-1out.html", title="Event form", message="Invalid ID"
        )

    response = make_response(template)
    response.set_cookie("prev_id", eventId)

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
    app.run(host="localhost", port=8500)
