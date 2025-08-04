class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_n = max(nums)
        res = 1
        counter = 0
        for n in nums:
          if n == max_n:
            counter += 1
            res = max(res, counter)
          else:
            counter = 0
        return res
