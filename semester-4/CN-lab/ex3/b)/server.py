import socket
import threading

HOST = 'localhost'
PORT = 65432

clients = []
client_lock = threading.Lock()

def handle_client(conn, addr):
  with conn:
    print('Connected by', addr)
    while True:
      data = conn.recv(1024)
      if not data:
        break
      client_lock.acquire()
      for client in clients:
        if client != conn:
          client.sendall(data + b"\nFrom: " + addr[0].encode())
      client_lock.release()
      print('Received from', addr, data.decode())
  client_lock.acquire()
  clients.remove(conn)
  client_lock.release()
  print('Client disconnected', addr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST, PORT))
  s.listen()
  print('Server started')
  while True:
    conn, addr = s.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
