from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import json
from typing import Dict, Optional
from datetime import datetime

class PasswordManager:
    def __init__(self, master_password: str):
        self.salt = self._get_or_create_salt()
        self.key = self._generate_key(master_password)
        self.fernet = Fernet(self.key)
        self.passwords_file = "passwords.enc"
        
    def _get_or_create_salt(self) -> bytes:
        if os.path.exists("salt.salt"):
            with open("salt.salt", "rb") as salt_file:
                return salt_file.read()
        
        salt = os.urandom(16)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
        return salt

    def _generate_key(self, master_password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        return key

    def add_password(self, service: str, username: str, password: str) -> None:
        passwords = self.get_all_passwords()
        passwords[service] = {
            "username": username,
            "password": password,
            "created_at": datetime.now().isoformat(),
            "last_modified": datetime.now().isoformat()
        }
        self._save_passwords(passwords)

    def get_password(self, service: str) -> Optional[Dict]:
        passwords = self.get_all_passwords()
        return passwords.get(service)

    def get_all_passwords(self) -> Dict:
        if not os.path.exists(self.passwords_file):
            return {}
        
        try:
            with open(self.passwords_file, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.fernet.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        except Exception:
            return {}

    def _save_passwords(self, passwords: Dict) -> None:
        encrypted_data = self.fernet.encrypt(json.dumps(passwords).encode())
        with open(self.passwords_file, "wb") as file:
            file.write(encrypted_data)

    def delete_password(self, service: str) -> bool:
        passwords = self.get_all_passwords()
        if service in passwords:
            del passwords[service]
            self._save_passwords(passwords)
            return True
        return False

    def update_password(self, service: str, new_password: str) -> bool:
        passwords = self.get_all_passwords()
        if service in passwords:
            passwords[service]["password"] = new_password
            passwords[service]["last_modified"] = datetime.now().isoformat()
            self._save_passwords(passwords)
            return True
        return False