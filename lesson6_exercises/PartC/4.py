
items = ["apple", "banana", "orange"]

# Old style
print("Old style:")
for i in range(len(items)):
    print(i, items[i])

# New style
print("\nNew style:")
for index, item in enumerate(items):
    print(index, item)

# Why is enumerate clearer?
# It gives both the index and the value directly, without needing to index into the list.
