from __future__ import annotations

from typing import Dict, Optional
from utils import load_data, save_data, Vault, Credential
from encryption import encrypt_password, decrypt_password
import string
import random

def generate_password(length: int = 12) -> str:
    if length <= 0:
        raise ValueError("length must be positive")
    characters: str = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def add_password() -> None:
    site: str = input("Site name: ")
    username: str = input("Username: ")
    password: str = input("Password: ")

    encrypted_password: str = encrypt_password(password)

    data: Vault = load_data()
    data[site] = {"username": username, "password": encrypted_password}
    save_data(data)
    print(f"✅ Password for '{site}' saved (encrypted).")

def view_passwords() -> None:
    data: Vault = load_data()
    if not data:
        print("No passwords saved.")
        return
    for site, creds in data.items():
        try:
            decrypted: str = decrypt_password(creds["password"])
            print(f"{site} → {creds['username']} / {decrypted}")
        except Exception as exc:
            print(f"{site} → Error decrypting password: {exc!s}")

def delete_password() -> None:
    site: str = input("Enter the site name to delete: ")
    data: Vault = load_data()

    if site in data:
        confirm: str = input(
            f"Are you sure you want to delete the credentials for '{site}'? (y/n): "
        ).lower()
        if confirm == "y":
            del data[site]
            save_data(data)
            print(f"🗑️ Deleted credentials for '{site}'.")
        else:
            print("❌ Deletion cancelled.")
    else:
        print(f"⚠️ No credentials found for '{site}'.")

def update_password() -> None:
    site: str = input("Enter the site name to update: ")
    data: Vault = load_data()

    if site in data:
        print(f"Current username: {data[site]['username']}")
        new_username: str = input("New username (press enter to keep current): ")
        new_password: str = input("New password (press enter to keep current): ")

        if new_username:
            data[site]["username"] = new_username
        if new_password:
            encrypted: str = encrypt_password(new_password)
            data[site]["password"] = encrypted

        save_data(data)
        print(f"✅ Credentials for '{site}' updated.")
    else:
        print(f"⚠️ No credentials found for '{site}'.")

def run_cli() -> None:
    while True:
        print("\n🔐 Password Manager")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Generate a secure password")
        print("4. Delete a saved password")
        print("5. Update existing password")
        print("6. Exit")

        choice: str = input("Select an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            try:
                length_str: str = input("Password length: ")
                length: int = int(length_str)
                print("Generated password:", generate_password(length))
            except ValueError:
                print("❌ Please enter a valid integer length.")
        elif choice == "4":
            delete_password()
        elif choice == "5":
            update_password()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
