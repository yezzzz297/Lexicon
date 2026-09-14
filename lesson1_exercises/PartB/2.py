price = float(input("Enter item price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print(f"Final price: {final_price:.2f}")