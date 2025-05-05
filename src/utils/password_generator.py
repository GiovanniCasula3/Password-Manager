import string
import secrets
from typing import Optional

class PasswordGenerator:
    @staticmethod
    def generate_password(
        length: int = 16,
        use_uppercase: bool = True,
        use_lowercase: bool = True,
        use_numbers: bool = True,
        use_special: bool = True,
        exclude_chars: Optional[str] = None
    ) -> str:
        if length < 8:
            raise ValueError("Password length must be at least 8 characters")

        chars = ""
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_numbers:
            chars += string.digits
        if use_special:
            chars += string.punctuation

        if exclude_chars:
            chars = ''.join(c for c in chars if c not in exclude_chars)

        if not chars:
            raise ValueError("No character set selected for password generation")

        # Ensure at least one character from each selected type
        password = []
        if use_uppercase:
            password.append(secrets.choice(string.ascii_uppercase))
        if use_lowercase:
            password.append(secrets.choice(string.ascii_lowercase))
        if use_numbers:
            password.append(secrets.choice(string.digits))
        if use_special:
            password.append(secrets.choice(string.punctuation))

        # Fill the rest of the password
        while len(password) < length:
            password.append(secrets.choice(chars))

        # Shuffle the password
        password_list = list(password)
        secrets.SystemRandom().shuffle(password_list)
        return ''.join(password_list)

    @staticmethod
    def check_password_strength(password: str) -> dict:
        strength = {
            "length": len(password) >= 12,
            "uppercase": any(c.isupper() for c in password),
            "lowercase": any(c.islower() for c in password),
            "numbers": any(c.isdigit() for c in password),
            "special": any(not c.isalnum() for c in password),
            "score": 0
        }
        
        strength["score"] = sum([
            strength["length"],
            strength["uppercase"],
            strength["lowercase"],
            strength["numbers"],
            strength["special"]
        ])
        
        return strength