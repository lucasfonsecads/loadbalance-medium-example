# server1.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response from server 1")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8001), SimpleHandler)
    print("Starting server 1 on port 8001")
    server.serve_forever()