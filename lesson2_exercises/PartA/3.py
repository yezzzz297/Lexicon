
password = "python123"

if password == "python123":
    print("Access granted")
else:
    print("Access denied")

grade = 88

if grade >= 50:
    print("Pass")
else:
    print("Fail")


languages = ["Python", "Java", "C++"]
languages.append("Ruby")
print(languages)

languages.insert(1, "C#")
print(languages)

languages.remove("Java")
print(languages)

languages.pop()
print(languages)