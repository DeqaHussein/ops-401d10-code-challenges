#!/usr/bin/env python3

import os

def search_files(file_name, directory):
    hits = 0
    files_searched = 0

    print(f"Searching for '{file_name}' in '{directory}':")

    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                print(f"Found: {file} | Location: {os.path.join(root, file)}")
            files_searched += 1

    print(f"\nTotal files searched: {files_searched}")
    print(f"Total hits found: {hits}")

if __name__ == "__main__":
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if os.name == "posix":  # Unix-based OS (e.g., Linux)
        search_fil
resource-chatgpt
