import pwd_functions

mode = input("Whoud you like to add a new passoerd, view an existing one or quit? (add/view/q): ").lower()
while True:
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        print("Goodbye!")
    else:
        print("Invalid mode.")
        continue
