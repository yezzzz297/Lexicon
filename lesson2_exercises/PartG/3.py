# Dictionary-based inventory for five products
inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15,
    "monitor": 8,
    "headset": 20
}

# Update stock values manually
inventory["laptop"] = 12
inventory["mouse"] = 30
inventory["keyboard"] = 18

# Calculate total units using the values in the dictionary
total_units = sum(inventory.values())

print("Inventory:", inventory)
print("Total units:", total_units)