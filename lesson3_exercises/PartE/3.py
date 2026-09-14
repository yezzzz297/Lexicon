#Repeating menu

choice = ""

while choice != "quit":
    print("1. Start")
    print("2. Help")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You selected Start")
    elif choice == "2":
        print("You selected Help")
    elif choice == "3":
        choice = "quit"
    else:
        print("Invalid choice")