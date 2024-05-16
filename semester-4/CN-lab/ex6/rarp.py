# Simulated RARP table
rarp_table = {
    '00:0a:95:9d:68:16': '192.168.1.1',
    '00:0a:95:9d:68:17': '192.168.1.2',
    '00:0a:95:9d:68:18': '192.168.1.3',
}

def sendRarpRequest(target_mac):
    if target_mac in rarp_table:
        return rarp_table[target_mac]
    else:
        return None

def main():
    target_mac = input("Enter target MAC address: ")
    ip_address = sendRarpRequest(target_mac)
    if ip_address:
        print(f"IP address for {target_mac} is {ip_address}")
    else:
        print(f"IP address for {target_mac} not found")

if __name__ == "__main__":
    main()


'''
OUTPUT:

Enter target MAC address: 00:0a:95:9d:68:16
IP address for 00:0a:95:9d:68:16 is 192.168.1.1


'''