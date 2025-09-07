class Solution:
    def sumZero(self, n: int) -> List[int]:
      res = []
      n, mod = divmod(n, 2)
      if mod:
        res.append(0)
      for i in range(1, n + 1):
        res.append(i)
        res.append(-i)
      return res