class Solution:
    def winnerSquareGame(self, n: int) -> bool:
      return self._dp(n)
        
    @cache
    def _dp(self, v):
      if v == 0:
        return False
      sqr = math.sqrt(v)
      for r in range(1, floor(sqr) + 1):
        supposed_a_pick = r * r
        remain = v - supposed_a_pick
        if not self._dp(remain):
          return True
      return False
      