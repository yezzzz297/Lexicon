correct_password = "python123"

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password")
    password = input("Try again: ")

print("Correct password!")