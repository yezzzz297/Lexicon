# Extend the base method with super()

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


admin = AdminUser("Ada", "ada@example.com", "Manager")
print(admin.get_information())
