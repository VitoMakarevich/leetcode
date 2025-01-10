class Solution:
    def canCross(self, stones: List[int]) -> bool:
      self._stones = stones
      self._cache = {}
      return self.internal(0, 0)
    
    
    def internal(self, pos, prev_jump):
      item = (pos, prev_jump)
      if not item in self._cache:
        next_jump_options = None
        if pos == len(self._stones) - 1:
          self._cache[item] = True
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
          if position - cur in next_jump_options:
            res = self.internal(idx, position - cur)
            if res:
              self._cache[item] = True
        if not item in self._cache:
          self._cache[item] = False
      return self._cache[item]