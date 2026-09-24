#Find duplicate values

numbers = [1, 2, 3, 2, 4, 5, 3, 6]

duplicates = []

for number in numbers:

    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicates:", duplicates)