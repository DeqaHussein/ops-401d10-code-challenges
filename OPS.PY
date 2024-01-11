import platform
import subprocess
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText

def ping(host):
    """
    Function to send an ICMP packet and check the response.
    """
    try:
        output = subprocess.check_output(["ping", "-n", "1", host])  # For Windows
        return True
    except subprocess.CalledProcessError:
        return False

def send_notification(email, password, host, status_before, status_after):
    """
    Function to send email notifications.
    """
    subject = f"Uptime Status Change - {host}"
    body = f"Host {host} status changed from {status_before} to {status_after} at {datetime.now()}."

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = email
    message["To"] = email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message.as_string())
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Error sending email notification: {e}")

def main():
    """
    Main function to run the uptime sensor tool.
    """
    email = input("Enter your email address: ")
    password = input("Enter your email password: ")

    host_to_check = "8.8.8.8"  # Replace with the IP address you want to monitor
    interval = 2  # Time interval in seconds
    current_status = None

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Format timestamp
        status = "Network Active" if ping(host_to_check) else "Network Inactive"
        
        if current_status is not None and current_status != status:
            send_notification(email, password, host_to_check, current_status, status)

        # Print the status with timestamp and destination IP
        print(f"{timestamp} {status} to {host_to_check}")

        current_status = status
        time.sleep(interval)  # Wait for the specified interval before the next check

if __name__ == "__main__":
    main()



New Email used was Deqarocks@gmail.com
Resource - Chatgpt. 
