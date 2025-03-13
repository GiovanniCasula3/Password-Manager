from pwd_functions import view, add
from master import get_fernet

master_pwd = input("Enter the master password: ")
fer = get_fernet(master_pwd)

while True:
    mode = input("Would you like to add a new password, view an existing one or quit? (add/view/q): ").lower()
    if mode == "view":
        view(fer)
    elif mode == "add":
        add(fer)
    elif mode == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid mode. Try again.")
