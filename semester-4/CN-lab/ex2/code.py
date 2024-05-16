import socket

def downloadWebpage(url):
    hostname = url.split("//")[1].split("/")[0]
    path = "/" + "/".join(url.split("//")[1].split("/")[1:])
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket creation failed with error:", err)
        return None

    try:
        s.connect((hostname, 80))
    except socket.gaierror as err:
        print("Failed to resolve hostname:", err)
        s.close()
        return None
    except socket.error as err:
        print("Connection error:", err)
        s.close()
        return None

    request = f"GET {path} HTTP/1.1\nHost: {hostname}\nConnection: close\n\n"
    s.sendall(request.encode())

    receivedData = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        receivedData += data

    s.close()

    with open("webpage.html", "wb") as f:
        f.write(receivedData)

    print("Webpage downloaded and saved to webpage.html")

url = input("Enter URL: ")
downloadWebpage(url)


'''
OUTPUT:

Enter URL: https://example.com
Webpage downloaded and saved to webpage.html


'''