# Part 6 - Sharing and copying

participants = ["Anna", "David", "Sara", "Leo", "Mia", "Noah", "Nora", "Oscar", "Lina", "Yusuf"]

# 1. Both variables use the same list.
backup_participants = participants
backup_participants.append("Ruth")
print("Original:", participants)
print("Backup:", backup_participants)

# 2. copy() makes a new list. 
backup_participants = participants.copy()
backup_participants.append("Paul")
print("Original:", participants)
print("Copy:", backup_participants)


records = [{"name": "Anna"}, {"name": "David"}]
backup_records = records.copy()
backup_records[0]["name"] = "Sara"
print("Original records:", records)
print("Copied records:", backup_records)
# Both show Sara because the inner dictionary was not copied.
