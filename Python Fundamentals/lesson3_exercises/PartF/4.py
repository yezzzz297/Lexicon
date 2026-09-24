#Skip negatives and stop at 999

numbers = [10, -5, 20, -3, 30, 999, 50]

for number in numbers:

    if number == 999:
        break

    if number < 0:
        continue

    print(number)