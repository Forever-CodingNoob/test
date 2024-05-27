import http.server
import socketserver

PORT = 48763
FILENAME = "rce.html"

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = FILENAME
        return super().do_GET()

Handler = CustomRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {FILENAME} on port {PORT}")
    httpd.serve_forever()

