import socket
import threading
DNS_RECORDS = {
  "www.google.com": "142.250.184.196",
  "www.example.com": "8.8.8.8",
  "www.mit.edu": "10.0.0.1",
}
HOST = 'localhost'
PORT = 53

def handle_client(conn, addr):
  with conn:
    data = conn.recv(1024)
    domain_name = data.decode().strip()
    print(f'Received request for domain: {domain_name} from {addr}')

    if domain_name in DNS_RECORDS:
      ip_address = DNS_RECORDS[domain_name]
      response = ip_address.encode()
    else:
      response = "Error: Domain not found".encode()

    conn.sendall(response)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind((HOST, PORT))
  print(f'DNS server started on {HOST}:{PORT}')
  while True:
    conn, addr = s.recvfrom(1024)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
