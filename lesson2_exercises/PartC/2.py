developer1 = {
    "Python",
    "Git",
    "SQL",
    "Docker"
}

developer2 = {
    "Python",
    "Java",
    "Git",
    "AWS"
}

common = developer1 & developer2
only_in_developer1 = developer1 - developer2
only_in_developer2 = developer2 - developer1

print("Same skills:", common)
print("Skills in first person:", only_in_developer1)
print("Skills in second person:", only_in_developer2)
