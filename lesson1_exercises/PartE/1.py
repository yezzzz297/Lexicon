first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
birth_year = input("Enter year of birth: ").strip()
language = input("Enter favourite programming language: ").strip()

full_name = f"{first_name} {last_name}"

user_id = (
    first_name[:3].lower()
    + last_name[:3].lower()
    + birth_year[-2:]
)

initials = first_name[0].upper() + last_name[0].upper()

name_length = len(first_name + last_name)

reversed_language = language[::-1]

current_year = 2026
age = current_year - int(birth_year)

city_upper = city.upper()

language_lower = language.lower()

print("\n--- Registration Summary ---")

print(f"Full name: {full_name}")
print(f"City: {city}")
print(f"Year of birth: {birth_year}")
print(f"Favourite language: {language}")
print(f"User ID: {user_id}")
print(f"Initials: {initials}")
print(f"Full name length: {name_length}")
print(f"Language reversed: {reversed_language}")

print(f"Approximate age: {age}")
print(f"City uppercase: {city_upper}")
print(f"Language lowercase: {language_lower}")