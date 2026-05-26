import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path.startswith('/?'):
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        print(f'[REQUEST] {args[0]} {args[1]}')

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public'))

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f'[*] Server running on http://0.0.0.0:{PORT}')
    print(f'[*] Press Ctrl+C to stop')
    httpd.serve_forever()
