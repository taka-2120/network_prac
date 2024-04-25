from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("a1-4.html", mode="r", encoding="utf-8") as file:
    input = file.read()
with open("a1-3.html", mode="r", encoding="utf-8") as file:
    output = file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面", message="")
        self.wfile.write(html.encode("utf-8"))
        return

    def do_POST(self):
        form = FieldStorage(
            fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
        )
        eventId = form["eventId"].value

        if eventId == "1":
            message = """
            <tr>
                <td>1</td>
                <td>予定1</td>
                <td>2024/04/01</td>
                <td>場所1</td>
            </tr>
            """
        elif eventId == "2":
            message = """
            <tr>
                <td>2</td>
                <td>予定2</td>
                <td>2024/04/02</td>
                <td>場所2</td>
            </tr>
            """
        elif eventId == "3":
            message = """
            <tr style=\"color:chocolate\">
                <td>3</td>
                <td>予定3</td>
                <td>2024/09/30</td>
                <td>場所3</td>
            </tr>
            """
        else:
            message = "<p>イベントIDが正しくありません。</p>"

        self.send_response(200)
        self.end_headers()
        html = output.format(title="イベント詳細", message=message)
        self.wfile.write(html.encode("utf-8"))
        return

    def error(self):
        self.send_error(404, "FILE NOT FOUND")

        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
