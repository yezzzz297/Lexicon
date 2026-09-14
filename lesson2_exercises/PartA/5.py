#sort() vs sorted()

numbers = [5, 2, 8, 1, 9]

# .sort() changes the original list
numbers.sort()
print(numbers)

# sorted() creates a new sorted list
numbers = [5, 2, 8, 1, 9]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)