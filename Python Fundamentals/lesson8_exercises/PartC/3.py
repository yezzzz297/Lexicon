# Create a savings account using super()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


account = SavingsAccount("Ada", 100, 0.03)
print(account.owner, account.balance, account.interest_rate)
