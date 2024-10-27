class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        existing = set()
        min_v = float('inf')
        for i in nums:
            if i > 0:
                min_v = min(min_v, i)
                existing.add(i)
        
        min_missing = float('inf')
        for i in nums:
            if i - 1 > 0 and not i - 1 in existing:
                min_missing = min(min_missing, i - 1)
            if i + 1 > 0 and not i + 1 in existing:
                min_missing = min(min_missing, i + 1)

        if min_v > 1:
            return 1
        else:
            return min_missing

        