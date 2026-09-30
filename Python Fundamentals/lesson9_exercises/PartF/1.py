# Create an Account class


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account = Account("Ada", 1000)
print(account.owner, account.balance)
