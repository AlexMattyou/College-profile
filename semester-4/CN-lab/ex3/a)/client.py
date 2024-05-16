import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = b'Hello, world!'
    s.sendall(message)
    data = s.recv(1024)

print('Received:', data.decode())


'''
OUTPUT:

Received: Hello, world!


'''