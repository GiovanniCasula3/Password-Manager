# Password Manager

A secure and easy-to-use password manager implemented in Python. This Password Manager uses advanced encryption to protect your passwords with a master key.

## Features

- Secure password encryption using Fernet (AES implementation)
- Master password protection
- Secure cryptographic salt generation and management
- Intuitive command-line interface
- Password addition and viewing functionality

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd Password-Manager
```

2. Install the required dependencies:
```bash
pip install cryptography
```

## Usage

1. Start the program:
```bash
python manager.py
```

2. Enter the master password when prompted

3. Choose one of the following options:
   - `add`: Add a new password
   - `view`: View an existing password
   - `q`: Exit the program

## Project Structure

- `manager.py`: Main script for the user interface
- `master.py`: Master password and encryption management
- `pwd_functions.py`: Password management functions
- `passwords.txt`: Encrypted file containing passwords
- `salt.salt`: File containing the cryptographic salt

## Security

- Passwords are encrypted using Fernet (AES)
- Unique cryptographic salt is utilized
- Master password is never stored
- Secure key derivation through PBKDF2

## Security Notes

- Keep your master password secure
- The `passwords.txt` file contains only encrypted data
- Cryptographic salt is automatically generated on first use

## Contributing

You are welcome to contribute to the project through pull requests or by reporting issues.