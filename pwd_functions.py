def view(fer):
    print("Insert the username for the password you want to see:")
    name = input("Enter the name of the account to view: ")
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                data = line.strip()
                if not data:
                    continue
                user, password = data.split(": ")
                if user == name:
                    decrypted = fer.decrypt(password.encode()).decode()
                    print("User: " + user + " | Password: " + decrypted)
                    break
            else:
                print("Password not found.")
    except FileNotFoundError:
        print("Il file delle password non esiste ancora.")

def add(fer):
    name = input("Enter the name of the account: ")
    pwd = input("Enter the password: ")
    encrypted = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + ": " + encrypted + "\n")
    print("Password added.")
