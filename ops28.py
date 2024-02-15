#!/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler
from scapy.all import *

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler for logging to a file
file_handler = RotatingFileHandler('logfile.log', maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a stream handler for logging to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Define formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
                    logger.info(f"Port {port} is open")
                    
                    # Send RST packet to gracefully close the open connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                # Closed port: Flag 0x14 (RST-ACK) received
                elif flags == 0x14:
                    logger.info(f"Port {port} is closed")
                # Filtered port: No flag received
                else:
                    logger.info(f"Port {port} is filtered and connection is silently dropped")

def main():
    logger.info("Network Security Tool Menu:")
    logger.info("1. TCP Port Range Scanner")
    choice = int(input("Enter your choice (1): "))

    if choice == 1:
        # TCP Port Range Scanner mode
        target_ip = input("Enter the target IP address: ")
        port_range_to_scan = tuple(map(int, input("Enter the port range (start end): ").split()))
        tcp_port_scanner(target_ip, port_range_to_scan)
    else:
        logger.error("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()



resource -chatgpt
