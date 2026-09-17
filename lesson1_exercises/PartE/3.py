
word = input("Enter a word: ").strip().lower()
reversed_word = word[::-1]

if word == reversed_word:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
