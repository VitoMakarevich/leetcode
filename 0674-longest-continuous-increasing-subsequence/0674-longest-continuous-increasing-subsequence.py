class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

      res = 0
      prev = nums[0]
      start = 0
      for idx, n in enumerate(nums[1:] + [-inf], start = 1):
        if n <= prev:
          res = max(res, idx - start)
          start = idx
        prev = n
      return res