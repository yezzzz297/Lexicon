
def build_sentence(separator, *words):
    """Join all words using the provided separator."""
    return separator.join(words)

print(build_sentence(", ", "Python", "is", "fun"))
print(build_sentence("-", "welcome", "to", "class"))
