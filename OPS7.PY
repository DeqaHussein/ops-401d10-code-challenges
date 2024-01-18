from cryptography.fernet import Fernet
import os
import shutil

def generate_key():
    return Fernet.generate_key()

def load_key(key_path):
    return open(key_path, "rb").read()

def save_key(key_path, key):
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_string(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    print("Encrypted Text:", encrypted_text.decode())

def decrypt_string(text, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(text.encode())
    print("Decrypted Text:", decrypted_text.decode())

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def main():
    key_path = "encryption_key.key"
    if not os.path.exists(key_path):
        key = generate_key()
        save_key(key_path, key)
    else:
        key = load_key(key_path)

    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    choice = int(input())

    if choice == 1 or choice == 2:
        file_path = input("Enter the file path: ")
        if choice == 1:
            encrypt_file(file_path, key)
        elif choice == 2:
            decrypt_file(file_path, key)

    elif choice == 3 or choice == 4:
        text = input("Enter the cleartext string: ")
        if choice == 3:
            encrypt_string(text, key)
        elif choice == 4:
            decrypt_string(text, key)

    elif choice == 5:
        folder_path = input("Enter the folder path: ")
        encrypt_folder(folder_path, key)

    elif choice == 6:
        folder_path = input("Enter the folder path: ")
        decrypt_folder(folder_path, key)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
