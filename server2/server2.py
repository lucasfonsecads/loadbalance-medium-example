# server2.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response from server 2")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8002), SimpleHandler)
    print("Starting server 2 on port 8002")
    server.serve_forever()