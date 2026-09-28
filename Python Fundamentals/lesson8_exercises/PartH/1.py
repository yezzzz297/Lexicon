# Start a user system with inheritance

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AdminUser(User):
    pass


class PremiumUser(User):
    pass


admin = AdminUser("Ada", "ada@example.com")
premium = PremiumUser("Sara", "sara@example.com")
print(admin.username, admin.email)
print(premium.username, premium.email)
