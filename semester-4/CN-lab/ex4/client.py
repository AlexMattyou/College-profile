import socket

HOST = 'localhost'
PORT = 53

def resolve_domain(domain_name):
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = domain_name.encode()
    s.sendto(message, (HOST, PORT))
    data, server = s.recvfrom(1024)
    return data.decode()

domain_name = input("Enter domain name: ")
ip_address = resolve_domain(domain_name)
if ip_address:
  print(f"IP address for {domain_name}: {ip_address}")
else:
  print(f"Error: Domain not found")
