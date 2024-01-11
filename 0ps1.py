import platform
import subprocess
from datetime import datetime
import time

def ping(host):
    """
    Function to send an ICMP packet and check the response.
    """
    try:
        output = subprocess.check_output(["ping", "-n", "1", host])  # For Windows
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """
    Main function to run the uptime sensor tool.
    """
    host_to_check = "8.8.8.8"  # Replace with the IP address you want to monitor
    interval = 2  # Time interval in seconds

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Format timestamp
        status = "Network Active" if ping(host_to_check) else "Network Inactive"
        
        # Print the status with timestamp and destination IP
        print(f"{timestamp} {status} to {host_to_check}")

        time.sleep(interval)  # Wait for the specified interval before the next check

if __name__ == "__main__":
    main()
