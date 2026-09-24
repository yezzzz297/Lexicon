stored_username = "admin"
stored_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == stored_username and password == stored_password:
    print("Login successful")
else:
    print("Login failed")