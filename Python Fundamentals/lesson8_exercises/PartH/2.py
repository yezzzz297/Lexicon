# Store a username and email

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


user = User("Grace", "grace@example.com")
print(user.username, user.email)
