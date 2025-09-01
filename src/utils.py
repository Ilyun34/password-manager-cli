from __future__ import annotations

from typing import Dict, TypedDict, Any, Final
import json
import os

FILE: Final[str] = "passwords.json"

class Credential(TypedDict):
    username: str
    password: str

# Vault is a mapping from site name to Credential
Vault = Dict[str, Credential]

def load_data() -> Vault:
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r", encoding="utf-8") as f:
        raw: Any = json.load(f)

    # Defensive normalization to Vault
    vault: Vault = {}
    if isinstance(raw, dict):
        for site, creds in raw.items():
            if (
                isinstance(site, str)
                and isinstance(creds, dict)
                and "username" in creds
                and "password" in creds
                and isinstance(creds["username"], str)
                and isinstance(creds["password"], str)
            ):
                vault[site] = {"username": creds["username"], "password": creds["password"]}
    return vault

def save_data(data: Vault) -> None:
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
