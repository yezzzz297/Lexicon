
def build_profile(name, age, city, country):
    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country,
    }


def build_profile_flexible(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile


print(build_profile("Ada", 22, "London", "UK"))
print(build_profile_flexible("Ada", age=22, city="London", country="UK"))

