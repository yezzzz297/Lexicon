total = float(input("Order total: "))
member = input("Are you a member? yes/no: ")

if (member == "yes" and total >= 50) or total >= 100:
    print("Free shipping")
else:
    print("Shipping fee applies")