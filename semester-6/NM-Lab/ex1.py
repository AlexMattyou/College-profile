import socket

def port_scanner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout for connection
            s.connect((ip, port))  # Try to connect to port
            print(f"[+] Port {port} is OPEN on {ip}")
    except:
        print(f"[-] Port {port} is CLOSED on {ip}")

# Example IP and Port Range
ip = "8.8.8.8"  # Google's public DNS
for port in range(45, 55):
    port_scanner(ip, port)

'''

[-] Port 45 is CLOSED on 8.8.8.8
...
[+] Port 53 is OPEN on 8.8.8.8  ← DNS port
...


'''