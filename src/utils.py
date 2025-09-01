from __future__ import annotations
from typing import Dict, TypedDict, Any, Final
from pathlib import Path
import json

DEFAULT_FILE: Final[Path] = Path("passwords.json")

class Credential(TypedDict):
    username: str
    password: str

# Vault is a mapping from site name to Credential
Vault = Dict[str, Credential]

def load_data() -> Vault:
    if not path.exists(path: Path = DEFAULT_FILE) -> Vault:
        return {}
    raw: Any = json.loads(path.read_text(encoding="utf-8"))

    # Defensive normalization to Vault
    vault: Vault = {}
    if isinstance(raw, dict):
        for site, creds in raw.items():
            if (
                isinstance(site, str)
                and isinstance(creds, dict)
                and "username" in creds
                and "password" in creds
            ):
                vault[site] = {
                    "username": str(creds["username"]),
                    "password": str(creds["password"])
                }
    return vault

def save_data(data: Vault, path: Path = DEFAULT_FILE) -> None:
    path.write_text(json.dumps(data, indent=4), encoding="utf-8")
