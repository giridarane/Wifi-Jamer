# Wifi-Jamer
This tool is a **Wi-Fi deauthentication (deauth) jammer** that can send deauth packets to a target device, disconnecting it from the Wi-Fi network. It is primarily designed for **educational and research purposes** to demonstrate how wireless networks can be attacked and how Wi-Fi security protocols can be tested.
The tool works by exploiting the deauthentication mechanism in the IEEE 802.11 Wi-Fi standard, which is commonly used to disconnect devices from a network. The tool is written in Python and uses the **Scapy** library to create and send custom packets.

> **Important:** **This tool should only be used in environments where you have explicit permission** to perform penetration testing or security auditing. Unauthorized use on networks or devices without consent is illegal and unethical. Please use responsibly.

## Features
- Sends deauth packets to a target MAC address, disconnecting it from the Wi-Fi network.
- Option to set the number of packets and the interval between them for customizable attacks.
- Enables monitor mode on your wireless interface for packet sniffing and injection.

## Installation

1. Clone the repository:
   ```bash
      git clone https://github.com/giridarane/Wifi-Jamer.git

   cd Wifi-Jamer

   pip install -r requirements.txt

You will be prompted to input:

The target MAC address (e.g., 00:11:22:33:44:55).
Your wireless interface (e.g., wlan0).
The number of deauth packets to send.
The interval between sending the packets.
The script will then start sending deauth packets to the target device.

Disclaimer
This tool is intended for educational and ethical hacking purposes only. Never use this tool on networks or devices you do not own or have explicit permission to test. Misuse of this tool can lead to legal consequences.

The author is not responsible for any damages or legal actions resulting from the use of this tool. Always follow ethical guidelines and obtain the necessary permissions before conducting any tests.
