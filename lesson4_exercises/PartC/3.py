
def create_profile(name, city="Unknown", active=True):
    """Build a dictionary with a person's details."""
    return {
        "name": name,
        "city": city,
        "active": active,
    }


print(create_profile("Ada"))
print(create_profile("Ada", "London", False))
