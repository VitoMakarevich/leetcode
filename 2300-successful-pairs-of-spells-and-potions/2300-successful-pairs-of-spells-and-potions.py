class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      potions.sort()
      mapping = [i for i in range(len(spells))]
      mapping.sort(key=lambda x: spells[x], reverse=True)
      res = [0] * len(spells)
      prev_start = 0
      for idx in mapping:
        sp = spells[idx]
        div, mod = divmod(success, sp)
        
        right_spell = bisect_left(potions, success / sp, lo = prev_start)
        prev_start = right_spell
        matching = len(potions) - right_spell
        res[idx] = matching
      return res