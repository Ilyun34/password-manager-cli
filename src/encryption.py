from __future__ import annotations
from typing import Final
from cryptography.fernet import Fernet
from pathlib import Path

DEFAULT_KEY_FILE: Final[Path] = Path("secret.key")

def generate_key(path: Path = DEFAULT_KEY_FILE) -> None:
    key: bytes = Fernet.generate_key()
    path.write_bytes(key)

def load_key(path: Path = DEFAULT_KEY_FILE) -> bytes:
    if not path.exists():
        generate_key(path)
    return path.read_bytes()

def encrypt_password(password: str, key_path: Path = DEFAULT_KEY_FILE) -> str:
    key: bytes = load_key(key_path)
    fernet: Fernet = Fernet(key)
    token: bytes = fernet.encrypt(password.encode("utf-8"))
    return token.decode("utf-8")

def decrypt_password(encrypted_password: str, key_path: Path = DEFAULT_KEY_FILE) -> str:
    key: bytes = load_key(key_path)
    fernet: Fernet = Fernet(key)
    plaintext: bytes = fernet.decrypt(encrypted_password.encode("utf-8"))
    return plaintext.decode("utf-8")
