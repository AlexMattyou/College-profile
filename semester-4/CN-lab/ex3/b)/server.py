import socket
import threading

HOST = 'localhost'
PORT = 65432

clients = []
clientLock = threading.Lock()

def handleClient(conn, addr):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            clientLock.acquire()
            for client in clients:
                if client != conn:
                    client.sendall(data + b"\nFrom: " + addr[0].encode())
            clientLock.release()
            print('Received from', addr, data.decode())
    clientLock.acquire()
    clients.remove(conn)
    clientLock.release()
    print('Client disconnected', addr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print('Server started')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()


'''
OUTPUT:

Server started
Connected by ('127.0.0.1', <port_number>)
Received from ('127.0.0.1', <port_number>) User1: Hello everyone!


'''