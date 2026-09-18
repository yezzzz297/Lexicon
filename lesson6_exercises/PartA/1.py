
squares = []
for number in range(1, 21):
    squares.append(number ** 2)
print("Loop version:", squares)

square_list = [number ** 2 for number in range(1, 21)]
print("Comprehension version:", square_list)
