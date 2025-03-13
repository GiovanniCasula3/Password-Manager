import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Se il file del sale non esiste, lo genera e lo salva
def write_salt():
    salt = os.urandom(16)
    with open("salt.salt", "wb") as salt_file:
        salt_file.write(salt)

def load_salt():
    if not os.path.exists("salt.salt"):
        write_salt()
    with open("salt.salt", "rb") as salt_file:
        return salt_file.read()

# Deriva la chiave Fernet a partire dal master password
def get_fernet(master_pwd):
    salt = load_salt()
    kdf = PBKDF2HMAC(
         algorithm=hashes.SHA256(),
         length=32,
         salt=salt,
         iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    return Fernet(key)
