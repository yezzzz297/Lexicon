supported_languages = ["Python", "Java", "C++", "JavaScript"]

language = input("Enter a programming language: ")

if language in supported_languages:
    print("Language is supported")
else:
    print("Language is not supported")