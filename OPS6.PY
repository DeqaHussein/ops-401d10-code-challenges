from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key", "rb").read()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    print("Encrypted Message:", encrypted_message.decode())

def decrypt_message(message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(message.encode())
    print("Decrypted Message:", decrypted_message.decode())

def main():
    if not os.path.isfile("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    mode = int(input("Select mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    if mode in [1, 2]:
        file_path = input("Enter the file path: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        elif mode == 2:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode in [3, 4]:
        user_input = input("Enter the message: ")
        if mode == 3:
            encrypt_message(user_input, key)
        elif mode == 4:
            decrypt_message(user_input, key)

if __name__ == "__main__":
    main()



  # Resource- Chatgpt
