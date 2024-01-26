#!/usr/bin/env python

from scapy.all import *

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
                    print(f"Port {port} is open")

                    # Send RST packet to gracefully close the open connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                # Closed port: Flag 0x14 (RST-ACK) received
                elif flags == 0x14:
                    print(f"Port {port} is closed")
                # Filtered port: No flag received
                else:
                    print(f"Port {port} is filtered and connection is silently dropped")

def network_security_tool():
    # Prompt user for an IP address to target
    target_ip = input("Enter the target IP address: ")

    # ICMP Ping
    icmp_packet = IP(dst=target_ip) / ICMP()
    response_packet = sr1(icmp_packet, timeout=1, verbose=0)

    if response_packet is None:
        print(f"Host {target_ip} is down or unresponsive.")
    elif response_packet.haslayer(ICMP):
        icmp_type = response_packet[ICMP].type
        icmp_code = response_packet[ICMP].code

        if icmp_type in [0, 8] and icmp_code == 0:
            print(f"Host {target_ip} is online.")

            # Run TCP Port Scanner
            port_range_to_scan = (1, 1024)  # Define the range of ports to scan
            tcp_port_scanner(target_ip, port_range_to_scan)
        elif icmp_type in [3, 9, 10, 13]:
            print(f"Host {target_ip} is actively blocking ICMP traffic.")
        else:
            print(f"Unexpected ICMP response: Type {icmp_type}, Code {icmp_code}")

if __name__ == "__main__":
    # Run the network security tool
    network_security_tool()


Resource-CHATGPT
