import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("a1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def getColor(self, sec):
        return "red" if sec % 2 == 0 else "black"

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        time = datetime.datetime.now()

        message = '<p style="color:{color}">{h}:{min}:{sec}</p>'.format(
            color=self.getColor(time.second),
            h=time.hour,
            min=time.minute,
            sec=time.second,
        )

        html = template.format(title="現在時刻", message=message)

        self.wfile.write(html.encode("utf-8"))

        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
