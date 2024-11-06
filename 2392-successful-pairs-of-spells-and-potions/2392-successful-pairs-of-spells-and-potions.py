class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells:
            min_multiplier = ceil(success/s)
            pos = bisect.bisect_left(potions, min_multiplier)
            count = len(potions) - pos
            
            res.append(count)

        return res