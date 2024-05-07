**Explanation:**

**Server (server.py):**

1. **DNS Records:** Defines a dictionary `DNS_RECORDS` to simulate a basic DNS database mapping domain names to IP addresses.
2. **Server Setup:**
   - Sets `HOST` and `PORT` for the server.
   - Creates a UDP socket.
   - Binds the socket to the specified address and port.
   - Starts a loop to handle client requests.
3. **Client Handling:**
   - A separate thread is created for each client request using `threading`.
   - Received data is decoded to get the requested domain name.
   - The server checks if the domain name exists in `DNS_RECORDS`.
   - If found, the corresponding IP address is encoded and sent back as a response.
   - If not found, an error message is sent back.

**Client (client.py):**

1. **Client Setup:**
   - Sets `HOST` and `PORT` for the DNS server.
   - Defines a function `resolve_domain` that takes a domain name as input.
2. **Sending Request:**
   - Creates a UDP socket.
   - Encodes the domain name and sends it to the DNS server address and port.
3. **Receiving Response:**
   - Receives the response from the server.
   - Decodes the received data to get the IP address or error message.
4. **Printing Result:**
   - If the IP address is found, it's printed along with the domain name.
   - If not found, an error message is displayed.

**Note:**

This code simulates a basic DNS server and client. Real DNS servers involve more complex protocols and security considerations.
