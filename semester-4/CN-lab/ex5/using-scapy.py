from scapy.all import sniff

def capturePackets(interface, count=10):
    packets = sniff(iface=interface, count=count)
    for packet in packets:
        print(f"Source: {packet.src}  Destination: {packet.dst}")
        print(f"Protocol: {packet.proto}")
        print("-" * 30)

interface = "en0"  # Change to the appropriate network interface
capturePackets(interface)


'''
OUTPUT:

Source: 192.168.1.2  Destination: 192.168.1.1
Protocol: 6
------------------------------
Source: 192.168.1.3  Destination: 192.168.1.4
Protocol: 17
------------------------------
...


'''