# Print both kinds of account

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner} - Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        # Let the parent class set up owner and balance.
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        information = super().__str__()
        return f"{information} - Interest rate: {self.interest_rate}%"


account = Account("Ada", 1000)
savings = SavingsAccount("Grace", 2000, 3)
print(account)
print(savings)
