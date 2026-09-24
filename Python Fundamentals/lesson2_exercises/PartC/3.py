skills = {"Python", "SQL", "Git"}


skills.add("Docker")
print(skills)

skills.remove("SQL")
print(skills)

skills.discard("Java")
print(skills)

print("Python" in skills)
print("Java" in skills)