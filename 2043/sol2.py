class Bank:
    def __init__(self, balance: List[int]):
        self.bank = balance
        self.n = len(balance)

    def valid(self, account: int) -> bool:
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid(account1) and self.valid(account2) and self.bank[account1 - 1] >= money:
            self.bank[account1 - 1] -= money
            self.bank[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid(account):
            self.bank[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid(account) and self.bank[account - 1] >= money:
            self.bank[account - 1] -= money
            return True
        return False
