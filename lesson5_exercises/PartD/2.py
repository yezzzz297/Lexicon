
def create_user(username, **details):
    
    user = {"username": username}
    user.update(details)
    return user

print(create_user("Ada", age=22, city="London"))
print(create_user("Johana", role="admin", active=True))
