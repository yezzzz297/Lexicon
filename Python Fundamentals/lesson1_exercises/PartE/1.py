
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
birth_year = input("Enter year of birth: ").strip()
language = input("Enter favourite programming language: ").strip()

full_name = first_name + " " + last_name
user_id = first_name[:3].lower() + last_name[:3].lower() + birth_year[-2:]
initials = first_name[0].upper() + last_name[0].upper()

print("Full name:", full_name)
print("City:", city)
print("Year of birth:", birth_year)
print("Favourite language:", language)
print("User ID:", user_id)
print("Initials:", initials)