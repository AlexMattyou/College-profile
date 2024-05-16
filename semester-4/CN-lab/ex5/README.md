Algorithm:
Import the sniff function from the scapy library.
Define a function capturePackets to capture network packets on a specified interface.
Use sniff to capture a specified number of packets on the given network interface.
Iterate through the captured packets, printing the source and destination IP addresses and the protocol used.
Call the capturePackets function with the desired network interface and packet count.