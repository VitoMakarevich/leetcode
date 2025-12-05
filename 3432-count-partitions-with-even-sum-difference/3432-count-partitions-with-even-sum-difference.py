class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        res = 0
        for idx in range(len(nums) - 1):
          right -= nums[idx]
          left += nums[idx]
          res += int((right - left) % 2 == 0)
        return res