
people = [
    {"first_name": "Marta", "last_name": "Jones"},
    {"first_name": "Abel", "last_name": "Isac"},
    {"first_name": "Sarah", "last_name": "Ada"},
]

sorted_people = sorted(people, key=lambda person: person["last_name"])
print(sorted_people)
