# First number divisible by 7 and 9

for number in range(1, 101):
    if number % 7 == 0 and number % 9 == 0:
        print("Found:", number)
        break