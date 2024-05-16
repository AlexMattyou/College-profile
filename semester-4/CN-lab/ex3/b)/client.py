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


'''
OUTPUT1:

Enter your username: User1
> Hello everyone!
User1: Hello everyone!
From: 127.0.0.1

OUTPUT2:

Enter your username: User2
> Hi User1!
User2: Hi User1!
From: 127.0.0.1

'''