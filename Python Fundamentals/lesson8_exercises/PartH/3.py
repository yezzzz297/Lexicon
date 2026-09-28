# Add a useful shared method

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_contact(self):
        return self.username + ": " + self.email


user = User("Grace", "grace@example.com")
print(user.get_contact())
