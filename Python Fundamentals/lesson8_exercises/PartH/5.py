# Add subclass attributes and methods using super()

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_contact(self):
        return self.username + ": " + self.email


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

    def manage_users(self):
        return self.username + " can manage users as " + self.role


class PremiumUser(User):
    def __init__(self, username, email, plan):
        super().__init__(username, email)
        self.plan = plan

    def watch_premium_video(self):
        return self.username + " can watch a video with the " + self.plan + " plan."


admin = AdminUser("Ada", "ada@example.com", "Manager")
premium = PremiumUser("Sara", "sara@example.com", "Gold")
print(admin.manage_users())
print(premium.watch_premium_video())
