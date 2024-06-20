from flask import Flask, make_response, render_template, request, session

app = Flask(__name__)
app.secret_key = "82b6c3ca-42ae-4ea4-b5e8-1654c90cabac"


@app.route("/", methods=["GET"])
def input():
    if "result" in session:
        result = session["result"]
    else:
        result = 0

    return render_template("a4-2.html", result=result)


@app.route("/", methods=["POST"])
def output():
    result = session["result"]
    if result is None:
        result = 0

    value = request.form["value"]
    operator = request.form["action"]
    if operator == "+":
        result = int(result) + int(value)
    elif operator == "-":
        result = int(result) - int(value)
    elif operator == "*":
        result = round(int(result) * int(value))
    else:
        result = round(int(result) / int(value))

    template = render_template("a4-2.html", result=result)

    response = make_response(template)
    session["result"] = result

    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8500)
