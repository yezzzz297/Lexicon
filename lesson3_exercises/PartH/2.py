#Count vowels

sentence = input("Enter a sentence: ")

vowels = "aeiou"
count = 0

for character in sentence.lower():

    if character in vowels:
        count += 1

print("Number of vowels:", count)