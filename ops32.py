#!/usr/bin/env python3

import os
import hashlib
import platform
from datetime import datetime

def search_file(filename, directory):
    hits = []
    searched_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                hits.append(os.path.join(root, file))
            searched_files += 1

    print("Hits:")
    for hit in hits:
        print(hit)

    print(f"\nFiles searched: {searched_files}")
    print(f"Hits found: {len(hits)}")

def scan_directory(directory):
    files_scanned = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5(file_path)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} | File: {file} | Size: {file_size} bytes | Path: {file_path} | MD5 Hash: {md5_hash}")
            files_scanned += 1

    print(f"\nTotal files scanned: {files_scanned}")

def generate_md5(filepath):
    hash_md5 = hashlib.md5()

    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory path to search in: ")

    if platform.system() == "Windows":
        filename = filename.replace("/", "\\")
        directory = directory.replace("/", "\\")

    print("\nSearching for files...")
    search_file(filename, directory)

    print("\nScanning directory for files and generating MD5 hashes...")
    scan_directory(directory)

if __name__ == "__main__":
    main()



resource-chatgpt
