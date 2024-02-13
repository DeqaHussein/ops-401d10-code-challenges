#!/usr/bin/env python3
import logging
from scapy.all import *

# Configure logging
logging.basicConfig(filename='scan_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def tcp_port_scanner(target_ip, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        # Crafting TCP SYN packet
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(dport=port, flags="S")

        # Sending packet and receiving response
        response_packet = sr1(ip_packet / tcp_packet, timeout=1, verbose=0)

        if response_packet is not None:
            # Check TCP flags in the response
            if response_packet.haslayer(TCP):
                flags = response_packet[TCP].flags

                # Open port: Flag 0x12 (SYN-ACK) received
                if flags == 0x12:
                    logging.info(f"Port {port} is open")
                    # Send RST packet to gracefully close the open connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                # Closed port: Flag 0x14 (RST-ACK) received
                elif flags == 0x14:
                    logging.info(f"Port {port} is closed")
                # Filtered port: No flag received
                else:
                    logging.info(f"Port {port} is filtered and connection is silently dropped")
        else:
            logging.error(f"No response received for port {port}")

def main():
    logging.info("Network Security Tool Menu:")
    logging.info("1. TCP Port Range Scanner")
    choice = int(input("Enter your choice (1): "))

    if choice == 1:
        # TCP Port Range Scanner mode
        target_ip = input("Enter the target IP address: ")
        port_range_to_scan = tuple(map(int, input("Enter the port range (start end): ").split()))
        tcp_port_scanner(target_ip, port_range_to_scan)
    else:
        logging.error("Invalid choice. Exiting.")



chatgpt-resource

if __name__ == "__main__":
    main()
