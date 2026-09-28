# Create two savings accounts

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


account1 = SavingsAccount("Ada", 100, 0.03)
account2 = SavingsAccount("Sara", 200, 0.04)
print(account1.owner, account1.balance, account1.interest_rate)
print(account2.owner, account2.balance, account2.interest_rate)
