import socket
import threading

DNS_RECORDS = {
    "www.google.com": "142.250.184.196",
    "www.example.com": "8.8.8.8",
    "www.mit.edu": "10.0.0.1",
}

HOST = 'localhost'
PORT = 53

def handleClient(data, addr):
    domainName = data.decode().strip()
    print(f'Received request for domain: {domainName} from {addr}')

    if domainName in DNS_RECORDS:
        ipAddress = DNS_RECORDS[domainName]
        response = ipAddress.encode()
    else:
        response = "Error: Domain not found".encode()

    s.sendto(response, addr)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f'DNS server started on {HOST}:{PORT}')
    while True:
        data, addr = s.recvfrom(1024)
        thread = threading.Thread(target=handleClient, args=(data, addr))
        thread.start()

'''
OUTPUT:

DNS server started on localhost:53
Received request for domain: www.example.com from ('127.0.0.1', 53)


'''