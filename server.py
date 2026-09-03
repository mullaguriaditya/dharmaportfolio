import http.server
import socketserver
import os

PORT = 8080

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.lower().endswith('.pdf'):
            filename = os.path.basename(self.path.split('?')[0])
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
        super().end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {PORT} with Content-Disposition...")
        httpd.serve_forever()
