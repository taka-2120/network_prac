from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("a6-1.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
