class Solution:
    def canCross(self, stones: List[int]) -> bool:
      self._stones = stones
      self._cache = [{} for i in range(len(stones))]
      return self.internal(0, 0)
    
    
    def internal(self, pos, prev_jump):
      item = (pos, prev_jump)
      if not prev_jump in self._cache[pos]:
        next_jump_options = None
        if pos == len(self._stones) - 1:
          self._cache[pos][prev_jump] = True
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
              self._cache[pos][prev_jump] = True
        if not prev_jump in self._cache[pos]:
          self._cache[pos][prev_jump] = False
      return self._cache[pos][prev_jump]