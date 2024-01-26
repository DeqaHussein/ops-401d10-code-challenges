#!/usr/bin/env python3
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

def icmp_ping_sweep(network_address):
    # Use scapy's method to generate a list of all addresses in the given network
    addresses = [str(ip) for ip in IP(network_address).hosts()]

    online_hosts = 0

    for address in addresses:
        # Skip network address and broadcast address
        if address.endswith('.0') or address.endswith('.255'):
            continue

        # Crafting ICMP Echo Request packet
        icmp_packet = IP(dst=address) / ICMP()

        # Sending packet and receiving response
        response_packet = sr1(icmp_packet, timeout=1, verbose=0)

        if response_packet is None:
            print(f"Host {address} is down or unresponsive.")
        elif response_packet.haslayer(ICMP):
            icmp_type = response_packet[ICMP].type
            icmp_code = response_packet[ICMP].code

            # ICMP Type 3 and Code 1,2,3,9,10,13 indicates actively blocking ICMP traffic
            if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {address} is actively blocking ICMP traffic.")
            else:
                print(f"Host {address} is responding.")
                online_hosts += 1

    print(f"\nTotal online hosts: {online_hosts}")

def main():
    print("Network Security Tool Menu:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        # TCP Port Range Scanner mode
        target_ip = input("Enter the target IP address: ")
        port_range_to_scan = tuple(map(int, input("Enter the port range (start end): ").split()))
        tcp_port_scanner(target_ip, port_range_to_scan)
    elif choice == 2:
        # ICMP Ping Sweep mode
        network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
