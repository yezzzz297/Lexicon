
def count_characters(text):
    """Return a dictionary with each character and its frequency."""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


print(count_characters("banana"))
