# Create a base account

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account = Account("Ada", 100)
print(account.owner, account.balance)
