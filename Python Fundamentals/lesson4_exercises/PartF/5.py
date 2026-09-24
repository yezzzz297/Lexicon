
def add_numbers(a: int, b: int) -> int:
    return a + b


def is_even(number: int) -> bool:
    return number % 2 == 0


def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


def average_score(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


print(add_numbers(2, 3))
print(is_even(8))
print(full_name("Ada", "Anna"))
print(average_score([10, 20, 30]))
print(count_characters("hello"))
