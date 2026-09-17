users1 = ["anna", "adam", "sara", "david", "abel"]

users2 = ["adam", "sara", "peter", "emma", "abel"]

set1 = set(users1)
set2 = set(users2)

duplicates = set1 & set2


unique_users = set1 | set2

print("Duplicates:", duplicates)
print("Unique usernames:", unique_users)