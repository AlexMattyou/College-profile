# TO RUN THIS CODE YOU NEED TO INSTALL WIRESHARK FOR WINDOWS
# OR ELSE USE ANOTHER VERSION WITH SCAPY
import subprocess

def capture_packets(interface, duration=10):
    
  """Captures packets on the specified interface using Wireshark (requires Wireshark to be installed)."""
  command = f"wireshark -i {interface} -d {duration} -w capture.pcap"
  subprocess.run(command.split(), check=True)
  print(f"Captured packets for {duration} seconds. Check 'capture.pcap' file using Wireshark.")

interface = "en0"
duration = 10
capture_packets(interface, duration)