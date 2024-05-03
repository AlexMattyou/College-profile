import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  username = input("Enter your username: ")

  while True:
    message = input('> ')
    if message == 'quit':
      break
    data = (username + ": " + message).encode()
    s.sendall(data)
    data = s.recv(1024)
    print(data.decode())

print('Disconnected from server')
