from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("a1-3.html", mode="r", encoding="utf-8") as file:
    template = file.read()


routes = []


def route(path, method):
    routes.append((path, method))


route("/id1", "id1")
route("/id2", "id2")
route("/id3", "id3")


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)

        for r in routes:

            if r[0] == _url.path:
                eval("self." + r[1] + "()")

                break

        else:
            self.error()

    def id1(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="イベント1",
            message="""
            <tr>
                <td>1</td>
                <td>予定1</td>
                <td>2024/04/01</td>
                <td>場所1</td>
            </tr>
            """,
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="イベント2",
            message="""
            <tr>
                <td>2</td>
                <td>予定2</td>
                <td>2024/04/02</td>
                <td>場所2</td>
            </tr>
            """,
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(
            title="イベント3",
            message="""
            <tr style=\"color:chocolate\">
                <td>3</td>
                <td>予定3</td>
                <td>2024/09/30</td>
                <td>場所3</td>
            </tr>
            """,
        )
        self.wfile.write(html.encode("utf-8"))
        return

    def error(self):
        self.send_error(404, "FILE NOT FOUND")

        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
