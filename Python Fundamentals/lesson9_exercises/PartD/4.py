# Print the isinstance() results

class User:
    pass


class AdminUser(User):
    pass


admin = AdminUser()

is_admin = isinstance(admin, AdminUser)
is_user = isinstance(admin, User)
is_string = isinstance(admin, str)

print(is_admin)   # True
print(is_user)    # True
print(is_string)  # False
