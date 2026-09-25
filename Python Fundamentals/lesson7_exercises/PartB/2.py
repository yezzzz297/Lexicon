# Deposit money

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

account = BankAccount("Yetnayet", 100)
account.deposit(50)
print(account.owner, account.balance)
