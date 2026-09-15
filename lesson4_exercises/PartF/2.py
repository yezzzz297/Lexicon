
def is_palindrome(word):
    """Return True if the word is a palindrome."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("java"))
print(is_palindrome("python"))
