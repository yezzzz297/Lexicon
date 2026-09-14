word = input("Enter a word: ")

middle_length = len(word) - 4

masked_word = word[:2] + "*" * middle_length + word[-2:]

print(masked_word)