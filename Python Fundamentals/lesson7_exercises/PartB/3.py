# Withdraw money without a negative balance

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

account = BankAccount("Yetnayet", 100)
account.withdraw(40)
print("Balance:", account.balance)
try:
    account.withdraw(100)
except ValueError as error:
    print(error)
print("Balance after rejected withdrawal:", account.balance)
