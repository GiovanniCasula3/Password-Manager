import argparse
import getpass
from ..core.password_manager import PasswordManager
from ..utils.password_generator import PasswordGenerator

def main():
    parser = argparse.ArgumentParser(description="Secure Password Manager")
    parser.add_argument("action", choices=["add", "get", "list", "delete", "update", "generate"])
    parser.add_argument("--service", help="Service name")
    parser.add_argument("--username", help="Username")
    parser.add_argument("--password", help="Password (if not provided, will be prompted)")
    parser.add_argument("--length", type=int, default=16, help="Password length for generation")
    
    args = parser.parse_args()
    
    # Get master password
    master_password = getpass.getpass("Enter master password: ")
    pm = PasswordManager(master_password)

    if args.action == "add":
        if not args.service or not args.username:
            print("Service and username are required for adding passwords")
            return
        
        password = args.password or getpass.getpass("Enter password: ")
        pm.add_password(args.service, args.username, password)
        print(f"Password added for {args.service}")

    elif args.action == "get":
        if not args.service:
            print("Service name is required")
            return
        
        password_data = pm.get_password(args.service)
        if password_data:
            print(f"Service: {args.service}")
            print(f"Username: {password_data['username']}")
            print(f"Password: {password_data['password']}")
        else:
            print(f"No password found for {args.service}")

    elif args.action == "list":
        passwords = pm.get_all_passwords()
        if passwords:
            for service, data in passwords.items():
                print(f"\nService: {service}")
                print(f"Username: {data['username']}")
                print(f"Created: {data['created_at']}")
                print(f"Last Modified: {data['last_modified']}")
        else:
            print("No passwords stored")

    elif args.action == "delete":
        if not args.service:
            print("Service name is required")
            return
        
        if pm.delete_password(args.service):
            print(f"Password deleted for {args.service}")
        else:
            print(f"No password found for {args.service}")

    elif args.action == "update":
        if not args.service:
            print("Service name is required")
            return
        
        new_password = args.password or getpass.getpass("Enter new password: ")
        if pm.update_password(args.service, new_password):
            print(f"Password updated for {args.service}")
        else:
            print(f"No password found for {args.service}")

    elif args.action == "generate":
        generator = PasswordGenerator()
        password = generator.generate_password(length=args.length)
        strength = generator.check_password_strength(password)
        print(f"Generated password: {password}")
        print(f"Password strength score: {strength['score']}/5")

if __name__ == "__main__":
    main()