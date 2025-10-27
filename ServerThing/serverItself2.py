from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response_(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        return 0

    def do_GET(self):
        return 0


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8080):
    return 0
