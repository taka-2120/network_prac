from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

with open("b8-1.html", mode="r", encoding="utf-8") as file:
    output = file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        event_id = int(query.get("id", ["1"])[0])

        self.send_response(200)

        if event_id == 1:
            data = """
            <tr>
                <td>1</td>
                <td>予定1</td>
                <td>2024/04/01</td>
                <td>場所1</td>
            </tr>
            """
        elif event_id == 2:
            data = """
            <tr>
                <td>2</td>
                <td>予定2</td>
                <td>2024/04/02</td>
                <td>場所2</td>
            </tr>
            """
        elif event_id == 3:
            data = """
            <tr style=\"color:chocolate\">
                <td>3</td>
                <td>予定3</td>
                <td>2024/09/30</td>
                <td>場所3</td>
            </tr>
            """
        else:
            data = "<p>イベントIDが正しくありません。</p>"

        self.send_response(200)
        self.end_headers()
        html = output.format(title="イベント詳細", data=data)
        self.wfile.write(html.encode("utf-8"))

        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
