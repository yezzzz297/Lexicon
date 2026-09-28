# Demonstrate all three kinds of methods

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_contact(self):
        return self.username + ": " + self.email

    def get_information(self):
        return "User: " + self.username


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

    def manage_users(self):
        return self.username + " can manage users as " + self.role

    def get_information(self):
        information = super().get_information()
        return information + " - Admin role: " + self.role


class PremiumUser(User):
    def __init__(self, username, email, plan):
        super().__init__(username, email)
        self.plan = plan

    def watch_premium_video(self):
        return self.username + " can watch a video with the " + self.plan + " plan."

    def get_information(self):
        return "Premium user: " + self.username + " - Plan: " + self.plan


user = User("Grace", "grace@example.com")
admin = AdminUser("Ada", "ada@example.com", "Manager")
premium = PremiumUser("Sara", "sara@example.com", "Gold")


# Inherited methods
print(user.get_contact())
print(admin.get_contact())
print(premium.get_contact())

# Subclass-specific methods
print(admin.manage_users())
print(premium.watch_premium_video())

# Base and overridden methods
print(user.get_information())
print(admin.get_information())
print(premium.get_information())
