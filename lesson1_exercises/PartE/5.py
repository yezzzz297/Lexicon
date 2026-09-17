
name = input("Enter your full name: ").strip()
parts = name.split()
initials = "".join(part[0].upper() for part in parts)

print("Your name:", name)
print("Initials:", initials)
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
