#!/usr/bin/env python3

import time

def offensive_mode(wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(0.1)  # Add a delay between words (adjust as needed)

def defensive_mode(search_string, wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        wordlist = [line.strip() for line in file]
        if search_string in wordlist:
            print(f'The password "{search_string}" was recognized.')
        else:
            print(f'The password "{search_string}" was not found in the word list.')

def main():
    print("Select Mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")

    mode = input("Enter the mode (1 or 2): ")

    if mode == '1':
        wordlist_path = input("Enter the path to the word list file: ")
        offensive_mode(wordlist_path)
    elif mode == '2':
        search_string = input("Enter the password to search: ")
        wordlist_path = input("Enter the path to the word list file: ")
        defensive_mode(search_string, wordlist_path)
    else:
        print("Invalid mode. Please choose 1 or 2.")

if __name__ == "__main__":
    main()


Resource-chatgpt
