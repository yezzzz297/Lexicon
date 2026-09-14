#Reference vs copy
list_a = [1, 2, 3]

list_b = list_a

list_b.append(4)

print("list_a:", list_a)
print("list_b:", list_b)