
sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("Number of vowels:", count)
