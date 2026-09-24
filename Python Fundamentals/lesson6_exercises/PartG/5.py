
numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]
print("Squares:", squares)

print("Total:", sum(numbers))
print("Any greater than 4?", any(n > 4 for n in numbers))

letters = {ch: ord(ch) for ch in "abc"}
print("Letters:", letters)

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)
