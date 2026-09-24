
def get_long_words(words, minimum_length):
    """Return a list of words that meet the length requirement."""
    result = []
    for word in words:
        if len(word) >= minimum_length:
            result.append(word)
    return result


print(get_long_words(["lion", "elephant", "dog", "tiger"], 5))
