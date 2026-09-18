
names = ["Laptop", "Phone", "Tablet"]
prices = [1200, 800, 450]
stocks = [5, 12, 9]

for name, price, stock in zip(names, prices, stocks):
    print(f"{name}: price={price}, stock={stock}")
