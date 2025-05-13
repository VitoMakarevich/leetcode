class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

      res = 0
      stack = []
      for idx in range(len(nums)):
        while not stack or nums[idx] < nums[stack[-1]]:  
          stack.append(idx)
      for idx in range(len(nums) - 1, -1, -1):
        while stack and nums[idx] >= nums[stack[-1]]:
          res = max(res, idx - stack.pop())
      return res