Algorithm:
Server:
Bind a UDP socket to the specified host and port.
Wait for incoming data packets containing domain name queries.
Check if the domain name exists in the DNS records and send the corresponding IP address back to the client, or an error message if the domain is not found.

Client:
Create a UDP socket and send the domain name query to the server.
Receive the response from the server and display the resolved IP address or an error message.