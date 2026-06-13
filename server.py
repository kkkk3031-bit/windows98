import http.server, socketserver, os

PORT = int(os.environ.get("PORT", "8000"))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
    print(f"Serving on 0.0.0.0:{PORT}")
    httpd.serve_forever()
