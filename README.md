# 🔐 Password Manager CLI

A simple command-line password manager written in Python.  
Securely stores credentials for your favorite websites and services in an encrypted JSON file.

---

## ✨ Features

- ✅ Add and store credentials (site, username, password)
- 🔐 Encrypt passwords before saving (AES encryption via `cryptography`)
- 🔓 Decrypt and view stored credentials
- 🔁 Generate strong, random passwords
- 🗑️ Delete saved passwords
- ✏️ Update credentials for existing entries
- 🧠 Local storage using `passwords.json`
- 📁 Encryption key auto-generated and stored in `secret.key`

---

## 📁 Project Structure

password-manager/
├── main.py          # Entry point
├── src/             # Source directory
  ├── cli.py           # CLI interface (add, view, generate)
  ├── utils.py         # JSON data load/save
  ├── encryption.py    # Encryption & decryption logic
  ├── passwords.json   # Encrypted credentials (auto-generated)
  ├── secret.key       # Encryption key (auto-generated)
  ├── .gitignore       # Excludes sensitive files from version control
  └── README.md





