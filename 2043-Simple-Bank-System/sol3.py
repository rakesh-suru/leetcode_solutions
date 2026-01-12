class Bank:
    def __init__(self, balance: List[int]):
        self.bank = {i + 1: bal for i, bal in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.bank and account2 in self.bank and self.bank[account1] >= money:
            self.bank[account1] -= money
            self.bank[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.bank:
            self.bank[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.bank and self.bank[account] >= money:
            self.bank[account] -= money
            return True
        return False
