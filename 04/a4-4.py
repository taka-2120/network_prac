from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    return render_template("a4-4.html", title="イベント登録")


@app.route("/", methods=["POST"])
def output():
    date = request.form["date"]
    event = request.form["event"]

    with open("a4-3.txt", "a", encoding="utf-8") as file:
        file.write(f"{date},{event}\n")

    return render_template("a4-4.html", title="イベント登録", message="登録しました。")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
