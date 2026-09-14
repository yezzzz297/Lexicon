email = input("Enter email: ")

at_position = email.index("@")

username = email[:at_position]
domain = email[at_position + 1:]

print("Username:", username)
print("Domain:", domain)