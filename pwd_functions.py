from master import master_pwd

def view():
    print("Insert the username for the password you want to see:")
    name = input("Enter the mail of the password: ")
    with open("passwords.txt", "r") as f:
        for line in f:
            data = line.strip()
            user, password = data.split(": ")
            if user == name:
                print(f"The password for {user} is {password}")
                break
        else:
            print("Password not found.")

def add():
    print("Adding a new password:")
    name = input("Enter the account of the password: ")
    pwd = input("Enter the password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{name}: {pwd}\n")
    print("Password added.")