# Check three type relationships

class User:
    pass


class AdminUser(User):
    pass


admin = AdminUser()

is_admin = isinstance(admin, AdminUser)
is_user = isinstance(admin, User)
is_string = isinstance(admin, str)
