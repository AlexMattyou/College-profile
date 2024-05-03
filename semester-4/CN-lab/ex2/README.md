Code for downloading a webpage using TCP sockets:

1. **Import and Function:**
   - Imports the `socket` library for network connections.
   - Defines a function `download_webpage` that takes a URL as input.

2. **Extracting Webpage Details:**
   - Splits the URL to extract the hostname (server address) and path (specific webpage location).

3. **Socket Creation and Connection:**
   - Creates a TCP socket connection.
   - Attempts to connect the socket to the server's hostname (default port 80 for HTTP).
   - Handles errors during socket creation or connection attempts.

4. **Sending HTTP Request:**
   - Constructs an HTTP GET request message specifying the path and hostname.
   - Adds a "Connection: close" header to indicate closing the connection after receiving the response.
   - Sends the encoded request message to the server.

5. **Receiving and Saving Webpage:**
   - Receives data chunks from the server in a loop.
   - Stores the received data in a byte array.
   - Closes the connection.
   - Saves the downloaded data (bytes) to a file named "webpage.html".