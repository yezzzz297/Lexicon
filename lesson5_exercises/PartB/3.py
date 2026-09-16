
def longest_word(*words):
    if not words:
        return None

    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("cat", "elephant", "dog"))
print(longest_word())
