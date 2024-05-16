Algorithm:
Extract the hostname and path from the given URL.
Create and connect a TCP socket to the hostname on port 80.
Send an HTTP GET request to fetch the web page.
Receive the response in chunks and concatenate them.
Save the received data to a file named "webpage.html".