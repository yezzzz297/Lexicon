
def get_active_users(users):
    """Return only the users who are active."""
    active_users = []
    for user in users:
        if user.get("active") is True:
            active_users.append(user)
    return active_users


users = [
    {"name": "A", "active": True},
    {"name": "B", "active": False},
    {"name": "C", "active": True},
]

print(get_active_users(users))
