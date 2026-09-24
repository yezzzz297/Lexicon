# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through each product.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    value = price * stock
# 4. Print the total value.
# 5. Find the most expensive in-stock product and print its name.

# Write your solution below:

total_value = 0
most_expensive_name = ""
most_expensive_price = 0

print("Products in stock:")
for product in products:
    if product["stock"] > 0:
        print(product["name"])
        total_value += product["price"] * product["stock"]

        if product["price"] > most_expensive_price:
            most_expensive_price = product["price"]
            most_expensive_name = product["name"]

print("Total value of products in stock:", total_value)
print("Most expensive in-stock product:", most_expensive_name)

# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average.
# It should receive a list of numbers and return the average.
#
# Create another function called create_result.
# It should call calculate_average() and return PASS if the average is 70 or more.
# Otherwise, it should return FAIL.
#
# Call create_result() using the scores above.
# Print both the average score and the final result.

# Write your solution below:

def calculate_average(list_of_scores):
    total = 0
    for score in list_of_scores:
        total += score

    average = total / len(list_of_scores)
    return average


def create_result(list_of_scores):
    average = calculate_average(list_of_scores)

    if average >= 70:
        return "PASS"
    else:
        return "FAIL"


average_score = calculate_average(scores)
result = create_result(scores)

print("Average score:", average_score)
print("Final result:", result)

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order.
# It receives:
# - a customer name
# - many product prices with *args
# - extra settings with **kwargs
#
# The function should:
# - add all prices to get the subtotal
# - apply the discount if it exists
# - add shipping if it exists
# - return a dictionary with customer, subtotal, final_total, and settings
#
# Call the function with:
# - customer name "Anna"
# - all prices from product_prices
# - all settings from order_settings
#
# Print the returned dictionary.

# Write your solution below:

def calculate_order(customer_name, *prices, **settings):
    subtotal = 0
    for price in prices:
        subtotal += price

    final_total = subtotal

    if "discount" in settings:
        discount_percent = settings["discount"]
        final_total = final_total - (final_total * discount_percent / 100)

    if "shipping" in settings:
        final_total = final_total + settings["shipping"]

    order = {
        "customer": customer_name,
        "subtotal": subtotal,
        "final_total": final_total,
        "settings": settings
    }

    return order


result = calculate_order("Anna", *product_prices, **order_settings)
print(result)

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Clean the player names.
#    Remove spaces and use correct capitalization.
#
# 2. Create a list of active players with score 80 or more.
#
# 3. Sort players by score from high to low.
#
# 4. Print the ranking like this:
#    1. Sara - 94
#    2. Emma - 88
#
# 5. Make a list of names and a list of scores, then print them together.

# Write your solution below:


print("Normalized names:")
for player in players:
    clean_name = player["name"].strip().title()
    print(clean_name)




print("Names and scores:")
for player in players:
    clean_name = player["name"].strip().title()
    print(clean_name, "-", player["score"])