from utils import load_data, save_data
from encryption import encrypt_password, decrypt_password
import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def add_password():
    site = input("Site name: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted_password = encrypt_password(password)

    data = load_data()
    data[site] = {"username": username, "password": encrypted_password}
    save_data(data)
    print(f"✅ Password for '{site}' saved (encrypted).")

def view_passwords():
    data = load_data()
    if not data:
        print("No passwords saved.")
        return
    for site, creds in data.items():
        decrypted = decrypt_password(creds['password'])
        print(f"{site} → {creds['username']} / {decrypted}")


def run_cli():
    while True:
        print("\n🔐 Password Manager")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Generate a secure password")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            length = int(input("Password length: "))
            print("Generated password:", generate_password(length))
        elif choice == '4':
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
