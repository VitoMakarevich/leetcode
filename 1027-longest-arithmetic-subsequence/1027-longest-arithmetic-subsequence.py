class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        cache = {}
        for right in range(len(nums)):
          for left in range(0, right):
            cache[(right, nums[right] - nums[left])] = cache.get((left, nums[right] - nums[left]), 1) + 1
        return max(cache.values())