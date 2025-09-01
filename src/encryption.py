from __future__ import annotations

from typing import Final
from cryptography.fernet import Fernet
import os

KEY_FILE: Final[str] = "secret.key"

def generate_key() -> None:
    key: bytes = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key() -> bytes:
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_password(password: str) -> str:
    key: bytes = load_key()
    fernet: Fernet = Fernet(key)
    token: bytes = fernet.encrypt(password.encode("utf-8"))
    return token.decode("utf-8")

def decrypt_password(encrypted_password: str) -> str:
    key: bytes = load_key()
    fernet: Fernet = Fernet(key)
    plaintext: bytes = fernet.decrypt(encrypted_password.encode("utf-8"))
    return plaintext.decode("utf-8")
