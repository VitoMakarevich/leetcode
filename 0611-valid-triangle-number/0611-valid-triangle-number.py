class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
      nums.sort()
      res = 0
      for idx1, s1 in enumerate(nums):
        for idx2, s2 in enumerate(nums[idx1 + 1:], start = idx1 + 1):
          max_to_fit_idx = bisect_left(nums, s1 + s2, idx2 + 1)
          res += max_to_fit_idx - idx2 - 1
      return res