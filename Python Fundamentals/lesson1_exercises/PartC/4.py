first_name = input("Enter first name: ").strip().lower()
last_name = input("Enter last name: ").strip().lower()

username = first_name[:3] + last_name[:5]

print("Username:", username)