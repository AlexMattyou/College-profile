import socket
import struct

# Simulated ARP table
arp_table = {
    '192.168.1.1': '00:0a:95:9d:68:16',
    '192.168.1.2': '00:0a:95:9d:68:17',
    '192.168.1.3': '00:0a:95:9d:68:18',
}

def sendArpRequest(target_ip):
    if target_ip in arp_table:
        return arp_table[target_ip]
    else:
        return None

def main():
    target_ip = input("Enter target IP address: ")
    mac_address = sendArpRequest(target_ip)
    if mac_address:
        print(f"MAC address for {target_ip} is {mac_address}")
    else:
        print(f"MAC address for {target_ip} not found")

if __name__ == "__main__":
    main()


'''
OUTPUT:

Enter target IP address: 192.168.1.1
MAC address for 192.168.1.1 is 00:0a:95:9d:68:16


'''