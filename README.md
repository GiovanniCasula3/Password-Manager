# Secure Password Manager

A robust and secure command-line password manager implemented in Python that provides encrypted storage for your passwords using advanced cryptographic techniques.

## Features

- Strong encryption using Fernet (AES-128)
- Secure password generation with customizable options
- Password strength evaluation
- Command-line interface for easy management
- Encrypted storage with master password protection
- Password history tracking with timestamps
- Secure salt management and key derivation

## Requirements

- Python 3.7 or higher
- Required packages:
```bash
pip install cryptography argon2-cffi PyYAML pytest python-dotenv
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd Password-Manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage Guide

### Basic Commands

1. Add a new password:
```bash
python -m src add --service "gmail" --username "user@gmail.com"
```
You will be prompted to enter the password securely.

2. View a stored password:
```bash
python -m src get --service "gmail"
```

3. List all services:
```bash
python -m src list
```

4. Delete a password:
```bash
python -m src delete --service "gmail"
```

5. Update a password:
```bash
python -m src update --service "gmail"
```

6. Generate a secure password:
```bash
python -m src generate --length 16
```

### Command Options

- `--service`: Service name (e.g., "gmail", "github")
- `--username`: Username for the service
- `--password`: Password (optional, will prompt if not provided)
- `--length`: Password length for generation (default: 16)

## Project Structure

```
Password-Manager/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli/
│   │   ├── __init__.py
│   │   └── interface.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── password_manager.py
│   └── utils/
│       ├── __init__.py
│       └── password_generator.py
├── requirements.txt
├── setup.py
└── README.md
```

## Security Features

### Password Protection
- AES-128 encryption using Fernet
- Secure key derivation (PBKDF2) with 100,000 iterations
- Cryptographic salt for added security
- Master password never stored

### Password Storage
- All passwords stored in encrypted format in `passwords.enc`
- Separate salt file (`salt.salt`) for enhanced security
- No plaintext password storage
- Automatic salt generation on first use

### Password Generation
- Minimum length of 8 characters
- Includes uppercase, lowercase, numbers, and special characters
- Uses cryptographically secure random number generation
- Password strength evaluation with 5 criteria:
  - Length (≥12 characters)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

## Best Practices

1. Master Password:
   - Use a strong, unique master password
   - Never share your master password
   - Change master password periodically

2. Generated Passwords:
   - Use generated passwords when possible
   - Minimum recommended length: 12 characters
   - Include all character types

## Security Notice

- Keep your master password secure
- Backup your encrypted files regularly
- Never share your salt.salt file
- Both `passwords.enc` and `salt.salt` files are required for operation
- These files are automatically excluded from git via .gitignore

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request