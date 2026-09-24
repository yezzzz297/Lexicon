
def count_words(*sections):
    total = 0
    for section in sections:
        if isinstance(section, str):
            total += len(section.split())
    return total


print(count_words("hello world", "Python is fun", "good luck"))
print(count_words("one two", "three four five"))
