#!/usr/bin/env python3

import os
import hashlib
import requests
import time

def search_directory(file_name, directory_path):
    hits = 0
    files_searched = 0

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                hits += 1
                print("Hit Found:")
                print(f"File Name: {file}")
                print(f"Location: {file_path}")

            files_searched += 1

    print(f"\nTotal files searched: {files_searched}")
    print(f"Total hits found: {hits}")

def calculate_file_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as f:
        buffer = f.read()
        hasher.update(buffer)

    return hasher.hexdigest()

def scan_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.islink(file_path):  # Exclude symbolic links
                file_size = os.path.getsize(file_path)
                file_md5 = calculate_file_hash(file_path)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

                print(f"Timestamp: {timestamp}")
                print(f"File Name: {file}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {file_md5}")
                print("-----------------------")

def virustotal_search(api_key, file_md5):
    url = f'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': file_md5}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        if result['response_code'] == 1:
            positives = result['positives']
            total = result['total']
            print(f"\nVirusTotal Scan Results:")
            print(f"Positives Detected: {positives}")
            print(f"Total Scanned: {total}")
        else:
            print("File not found on VirusTotal.")
    else:
        print("Error querying VirusTotal API")

def main():
    file_name = input("Enter the file name to search for: ")
    directory_path = input("Enter the directory to search in: ")

    search_directory(file_name, directory_path)
    scan_directory(directory_path)

    file_md5 = calculate_file_hash(os.path.join(directory_path, file_name))
    virustotal_search("YOUR_VIRUSTOTAL_API_KEY", file_md5)

if __name__ == "__main__":
    main()



resource-chatgpt
