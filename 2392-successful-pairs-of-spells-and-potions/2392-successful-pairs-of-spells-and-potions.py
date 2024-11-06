class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        cache = {}
        res = []
        for s in spells:
            if not s in cache:
                min_multiplier = ceil(success/s)
                pos = bisect.bisect_left(potions, min_multiplier)
                count = len(potions) - pos
                cache[s] = count
            res.append(cache[s])

        return res