import socket
import telnetlib
import subprocess

def netcat_banner_grabbing(target_host, target_port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to target
        s.connect((target_host, target_port))
        # Send a dummy data to trigger response
        s.send(b'GET / HTTP/1.1\r\n\r\n')
        # Receive banner
        banner = s.recv(1024)
        print("[*] Banner grabbed using Netcat:")
        print(banner.decode())
    except Exception as e:
        print("[!] Error:", e)
    finally:
        # Close the socket
        s.close()

def telnet_banner_grabbing(target_host, target_port):
    try:
        # Create a Telnet object
        tn = telnetlib.Telnet(target_host, target_port)
        # Read banner
        banner = tn.read_all()
        print("[*] Banner grabbed using Telnet:")
        print(banner.decode())
    except Exception as e:
        print("[!] Error:", e)

def nmap_banner_grabbing(target_host):
    try:
        # Run Nmap command
        nmap_command = f'nmap -sV {target_host}'
        result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
        print("[*] Banner grabbed using Nmap:")
        print(result.stdout)
    except Exception as e:
        print("[!] Error:", e)

if __name__ == "__main__":
    target_host = input("Enter the target URL or IP address: ")
    target_port = int(input("Enter the target port number: "))

    netcat_banner_grabbing(target_host, target_port)
    telnet_banner_grabbing(target_host, target_port)
    nmap_banner_grabbing(target_host)





resource-chatgpt
