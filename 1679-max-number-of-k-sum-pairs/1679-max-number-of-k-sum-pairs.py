class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_with_counts = Counter(nums)
        res = 0
        used = set()
        for item, amount in nums_with_counts.items():
            if item not in used:
                if k - item == item:
                    res += floor(amount / 2)
                elif nums_with_counts.get(k - item, 0) > 0:
                    res += min(amount, nums_with_counts[k - item])
                    used.add(k - item)

        return res