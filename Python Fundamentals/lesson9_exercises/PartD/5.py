# Explain why an admin is also a user

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

# AdminUser inherits from User, so an AdminUser IS-A User.
# isinstance() recognises both the child class and its parent class.
