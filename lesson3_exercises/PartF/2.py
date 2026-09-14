#Skip empty strings

words = ["Hello", "", "Python", "", "World"]

for word in words:
    if word == "":
        continue

    print(word)