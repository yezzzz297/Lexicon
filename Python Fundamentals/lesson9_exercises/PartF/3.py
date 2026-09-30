# Create SavingsAccount using super()

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


savings = SavingsAccount("yetnayet", 2000, 3)
print(savings.owner, savings.balance, savings.interest_rate)
