
numbers = [1, 2, 3, 4, 5, 6]
squares = [n * n for n in numbers]

evens = [n for n in numbers if n % 2 == 0]
doubles = [n * 2 for n in numbers]

print("Squares:", squares)
print("Evens:", evens)
print("Doubles:", doubles)
