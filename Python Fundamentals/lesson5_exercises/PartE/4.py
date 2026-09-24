
def describe_person(name, *details, **info):
    summary = {
        "name": name,
        "details": list(details),
    }
    summary.update(info)
    return summary


print(describe_person("Ada", "friendly", "kind", city="London", age=22))
print(describe_person("Sara", "student", "runner", city="Cairo", age=19))
print(describe_person("Anna", "artist", "traveler", city="Paris", age=25))
