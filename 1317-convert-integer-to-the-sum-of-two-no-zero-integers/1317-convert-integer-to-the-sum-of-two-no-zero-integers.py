class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
      for i in range(1, n + 1):
        if not self.has_zero(i) and not self.has_zero(n - i):
          return [i, n - i]
      
    def has_zero(self, num):
      while num > 0:
        div, mod = divmod(num, 10)
        if mod == 0:
          return True
        num = div
      return False