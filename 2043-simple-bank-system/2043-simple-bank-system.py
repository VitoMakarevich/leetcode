class Bank:

    def __init__(self, balance: List[int]):
      self.balances = balance

    def is_valid_account(self, account, amount):
      if account < 0 or account >= len(self.balances) or self.balances[account] + amount < 0:
        return False
      return True



    def transfer(self, account1: int, account2: int, money: int) -> bool:
      account1 -= 1
      account2 -= 1
      if not self.is_valid_account(account1, -money) or not self.is_valid_account(account2, money):
        return False
      self.balances[account1] -= money
      self.balances[account2] += money
      return True

    def deposit(self, account: int, money: int) -> bool:
      account -= 1
      if not self.is_valid_account(account, money):
        return False
      self.balances[account] += money
      return True
        

    def withdraw(self, account: int, money: int) -> bool:
      account -= 1
      if not self.is_valid_account(account, -money):
        return False
      self.balances[account] -= money
      return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)