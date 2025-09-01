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
        try:
            decrypted = decrypt_password(creds['password'])
            print(f"{site} → {creds['username']} / {decrypted}")
        except:
            print(f"{site} → Error decrypting password.")

def delete_password():
    site = input("Enter the site name to delete: ")
    data = load_data()

    if site in data:
        confirm = input(f"Are you sure you want to delete the credentials for '{site}'? (y/n): ").lower()
        if confirm == 'y':
            del data[site]
            save_data(data)
            print(f"🗑️ Deleted credentials for '{site}'.")
        else:
            print("❌ Deletion cancelled.")
    else:
        print(f"⚠️ No credentials found for '{site}'.")

def update_password():
    site = input("Enter the site name to update: ")
    data = load_data()

    if site in data:
        print(f"Current username: {data[site]['username']}")
        new_username = input("New username (press enter to keep current): ")
        new_password = input("New password (press enter to keep current): ")

        if new_username:
            data[site]['username'] = new_username
        if new_password:
            encrypted = encrypt_password(new_password)
            data[site]['password'] = encrypted

        save_data(data)
        print(f"✅ Credentials for '{site}' updated.")
    else:
        print(f"⚠️ No credentials found for '{site}'.")

def run_cli():
    while True:
        print("\n🔐 Password Manager")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Generate a secure password")
        print("4. Delete a saved password")
        print("5. Update existing password")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            length = int(input("Password length: "))
            print("Generated password:", generate_password(length))
        elif choice == '4':
            delete_password()
        elif choice == '5':
            update_password()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
