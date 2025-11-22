class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      potions.sort()
      res = []
      for sp in spells:
        div, mod = divmod(success, sp)
        
        right_spell = bisect_left(potions, success / sp)
        
        matching = len(potions) - right_spell
        res.append(matching)
      return res