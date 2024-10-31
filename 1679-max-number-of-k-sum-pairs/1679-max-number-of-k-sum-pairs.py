class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_with_counts = Counter(nums)
        cnt = len(nums)
        res = 0
        for v in nums:
            if v >= k:
                continue
            if nums_with_counts[v] > 0:
                nums_with_counts[v] -= 1
                if nums_with_counts.get(k - v, 0) > 0:
                    res += 1
                    nums_with_counts[k - v] -= 1
            else:
                nums_with_counts[v] -= 1
        return res