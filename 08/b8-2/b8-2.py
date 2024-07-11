import cgi
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("b8-2.html", mode="r", encoding="utf-8") as file:
    output = file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = """
        <form action="/" method="post">
            <label for="event_name">イベント名</label>
            <input type="text" name="event_name" id="event_name">
            <input type="date" name="event_date" id="event_date">
            <input type="submit">
        </form>
        """
        self.send_response(200)
        self.end_headers()
        html = output.format(title="イベント検索", response=response)
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
        )
        event_name = form["event_name"].value
        event_date_str = form["event_date"].value
        event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d")

        today = datetime.datetime.now()
        days_remaining = (event_date - today).days + 1

        response = f"<h2>{event_name}[{event_date.strftime("%Y/%m/%d")}]まで、あと{days_remaining}日です。</h2>"
        self.send_response(200)
        self.end_headers()
        html = output.format(title="イベント検索", response=response)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
