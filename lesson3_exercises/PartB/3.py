blocked_users = ["admin", "root", "guest", "test"]

username = input("Enter username: ")

if username in blocked_users:
    print("Username is blocked")
else:
    print("Username is allowed")