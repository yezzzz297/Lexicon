# Study menu

sessions = [
    {"subject": "Python", "minutes": 60},
    {"subject": "AI", "minutes": 45},
    {"subject": "SQL", "minutes": 30},
    {"subject": "Python", "minutes": 50},
    {"subject": "Machine Learning", "minutes": 70},
    {"subject": "AI", "minutes": 40},
    {"subject": "SQL", "minutes": 55},
    {"subject": "Python", "minutes": 80},
    {"subject": "AI", "minutes": 65},
    {"subject": "Machine Learning", "minutes": 90}
]

while True:
    print("\nStudy Menu")
    print("1. Show all sessions")
    print("2. Show total minutes")
    print("3. Find one subject")
    print("4. Exit")

    choice = input("Choose a number: ")

    if choice == "1":
        for session in sessions:
            print(session["subject"], session["minutes"])

    elif choice == "2":
        total = 0

        for session in sessions:
            total += session["minutes"]

        print("Total minutes:", total)

    elif choice == "3":
        subject = input("Enter subject: ")

        for session in sessions:
            if session["subject"].lower() == subject.lower():
                print(session)

    elif choice == "4":
        print("Bye")
        break

    else:
        print("Wrong choice")
