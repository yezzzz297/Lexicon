
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("java"))
print(is_palindrome("python"))
