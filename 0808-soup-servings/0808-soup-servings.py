class Solution:
    
    def soupServings(self, n: int) -> float:
      n = ceil(n / 25)
      self.changes = [(4, 0), (3, 1), (2, 2), (1, 3)]
      for k in range(1, n + 1):
        if self.dp(k, k) > 1 - 1e-5:
          return 1
      return self.dp(n, n)
    
    @cache
    def dp(self, a, b):
      if a <= 0 or b <= 0:
        return self.multipliers(a, b)
      res = 0
      for a_minus, b_minus in self.changes:
        res += self.dp(a - a_minus, b - b_minus)
      return res / 4
    
    def multipliers(self, a, b):
      if a <= 0 and b > 0:
        return 1
      elif a <= 0 and b <= 0:
        return 0.5
      return 0