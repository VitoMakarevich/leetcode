class Solution:
    
    def soupServings(self, n: int) -> float:
      if n > 5000:
        return 1
      n = ceil(n / 25)
      self.changes = [(4, 0), (3, 1), (2, 2), (1, 3)]
      
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