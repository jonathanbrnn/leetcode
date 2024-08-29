class Bank():

    def __init__(self, balance: List[int]):
        self.accounts = {}

        for i, bal in enumerate(balance):
            self.accounts[i+1] = bal

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.accounts and account2 in self.accounts:
            if money <= self.accounts[account1]:
                self.accounts[account2] += money
                self.accounts[account1] -= money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.accounts:
            self.accounts[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.accounts:
            if money <= self.accounts[account]:
                self.accounts[account] -= money
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
