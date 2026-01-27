import socket
import sys


host = "localhost"
port = 9090
data = "Sent from self"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(bytes(data, "utf-8"))
    print("All sent")
    received = str(sock.recv(1000), "utf-8")

print("Sent: ", data)
print("Received: ", received)
