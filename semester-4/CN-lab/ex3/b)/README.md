Algorithm:

Server:
Create and bind a socket to the specified host and port.
Listen for incoming connections and accept them in a loop.
Spawn a new thread for each client connection to handle communication.
Broadcast received messages to all connected clients except the sender.

Client:
Create and connect a socket to the server.
Continuously read user input and send messages to the server.
Receive and print messages broadcasted by the server.