import datetime

from flask import Flask, render_template, request

# flaskモジュールからFlaskクラスとrender_templateメソッドをインポートする

app = Flask(__name__)
# Flaskインスタンスを生成する.


@app.route("/", methods=["GET"])
def input():
    return render_template("a2-4in.html", title="Event form")


@app.route("/", methods=["POST"])
def output():
    eventId = request.form["eventId"]
    if eventId == "1":
        return event1()
    elif eventId == "2":
        return event2()
    elif eventId == "3":
        return event3()
    else:
        return render_template("a2-4out.html", title="Event form", message="Invalid ID")


def event1():
    return render_template(
        "a2-4out.html",
        title="イベント1",
        id=1,
        name="予定1",
        date="2024/04/01",
        place="場所1",
        future=False,
    )


def event2():
    return render_template(
        "a2-4out.html",
        title="イベント2",
        id=2,
        name="予定2",
        date="2024/04/02",
        place="場所2",
        future=False,
    )


def event3():
    return render_template(
        "a2-4out.html",
        title="イベント3",
        id=3,
        name="予定3",
        date="2024/09/30",
        place="場所3",
        future=True,
    )


if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost", port=8500)
    # ホスト名をlocalhostにして，Webアプリケーションを起動する．
