import socketserver


class somethingTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.readline(5000).rstrip()
        print(f"{self.client_address}: ")
        print(self.data.decode("utf-8"))
        self.wfile.write("received")


if __name__ == "__main__":
    host = "localhost"
    port = 9090
    with socketserver.TCPServer((host, port), somethingTCPHandler) as server:
        print("Started")
        server.serve_forever(5)
