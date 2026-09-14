# Search for a name

names = ["Anna", "John", "Sara", "David"]

target = "Sara"
found = False

for name in names:
    if name == target:
        print("found")
        found = True
        break

if not found:
    print("Name was not found")