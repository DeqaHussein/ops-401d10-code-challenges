#!/usr/bin/env python3
import time
import paramiko
import zipfile

def offensive_mode(wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        for word in wordlist:
            password = word.strip()
            print(f"Trying password: {password}")
            time.sleep(1)

      def zip_brute_force(zip_file_path, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            for password in wordlist:
                try:
                    zip_file.extractall(pwd=password.strip().encode('utf-8'))
                    print(f"Successful extraction! Password: {password.strip()}")
                    break
                except Exception as e:
                    print(f"Failed attempt with password: {password.strip()}")

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    # Commenting out defensive_mode and ssh_brute_force options
    # print("2. Defensive; Password Recognized")
    # print("3. SSH Brute Force")
    print("4. ZIP Brute Force")
    
    mode = int(input("Enter mode number: "))

    if mode == 1:
        wordlist_path = input("Enter word list file path: ")
        offensive_mode(wordlist_path)


elif mode == 4:
        zip_file_path = input("Enter path to the password-protected ZIP file: ")
        wordlist_path = input("Enter word list file path: ")
        zip_brute_force(zip_file_path, wordlist_path)
    else:
        print("Invalid mode selected.")


Reosource-chatgpt
