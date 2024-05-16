import socket

HOST = 'localhost'
PORT = 53

def resolveDomain(domainName):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = domainName.encode()
        s.sendto(message, (HOST, PORT))
        data, _ = s.recvfrom(1024)
        return data.decode()

domainName = input("Enter domain name: ")
ipAddress = resolveDomain(domainName)
if ipAddress:
    print(f"IP address for {domainName}: {ipAddress}")
else:
    print(f"Error: Domain not found")


'''
OUTPUT:

Enter domain name: www.example.com
IP address for www.example.com: 8.8.8.8


'''