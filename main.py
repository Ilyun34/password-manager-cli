import json
import random
import string
from utils import load_data, save_data

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def add_password(site, username, password):
    data = load_data()
    data[site] = {"username": username, "password": password}
    save_data(data)
    print("Password saved successfully.")

def view_passwords():
    data = load_data()
    for site, creds in data.items():
        print(f"{site} → {creds['username']} / {creds['password']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add new password")
        print("2. View all passwords")
        print("3. Generate a secure password")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            site = input("Site name: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(site, username, password)
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            length = int(input("Password length: "))
            print("Generated password:", generate_password(length))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
