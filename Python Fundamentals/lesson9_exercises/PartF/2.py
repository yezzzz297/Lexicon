# Add __str__ to Account

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner} - Balance: {self.balance}"


print(Account("Ada", 1000))
