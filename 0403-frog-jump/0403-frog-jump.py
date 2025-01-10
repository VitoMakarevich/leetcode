class Solution:
    def canCross(self, stones: List[int]) -> bool:
      self._stones = stones
      return self.internal(0, 0)
    
    @cache
    def internal(self, pos, prev_jump):
      next_jump_options = []
      if pos == len(self._stones) - 1:
        return True
      if prev_jump == 0:
        next_jump_options = [1]
      else:
        if prev_jump == 1:
          next_jump_options = [1, 2]
        else:
          next_jump_options = range(prev_jump - 1, prev_jump + 2)
      cur = self._stones[pos]
      for idx, position in enumerate(self._stones[pos + 1:], start = pos + 1):
        if position > cur + next_jump_options[-1]:
          break
        for opt in next_jump_options:
          if position - opt == cur:
            res = self.internal(idx, opt)
            if res:
              return True
      return False