#!/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler
from scapy.all import *

def setup_logging():
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a rotating file handler to manage log file size
    log_file = "scanner.log"
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

def tcp_port_scanner(target_ip, port_range, logger):
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
    # Setup logging
    logger = setup_logging()

    print("Network Security Tool Menu:")
    print("1. TCP Port Range Scanner")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        # TCP Port Range Scanner mode
        target_ip = input("Enter the target IP address: ")
        port_range_to_scan = tuple(map(int, input("Enter the port range (start end): ").split()))
        tcp_port_scanner(target_ip, port_range_to_scan, logger)
    else:
        logger.error("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()


Resource-chatgpt
