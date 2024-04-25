from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ("", 8000)

handler_class = SimpleHTTPRequestHandler

server = HTTPServer(server_address, handler_class)

server.serve_forever()
