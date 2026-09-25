# Part 7 - Global, local and enclosing scope

tax_rate = 0.15

def show_tax():
    print("Global:", tax_rate)


def show_local_tax():
    tax_rate = 0.10
    print("Local:", tax_rate)




def increase_tax(rate, increase):
    # Return the value instead of changing hidden global state.
    return rate + increase


def order_note():
    message = "Pack carefully"

    def show_note():
        print(message)  # From the enclosing function.

    show_note()


show_tax()
show_local_tax()
print("Global is unchanged:", tax_rate)
tax_rate = increase_tax(tax_rate, 0.05)
print("New rate:", round(tax_rate, 2))
order_note()
