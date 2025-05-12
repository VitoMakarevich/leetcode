class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 1
      if len(nums) == 1:
        return nums[0]
      def linear(nums):
        @cache
        def dp(index):
          if index >= len(nums):
            return 0
          if_rob_this = nums[index] + dp(index + 2)
          if_not_rob_this = dp(index + 1)
          return max(if_rob_this, if_not_rob_this)
        return dp(0)
      return max(linear(nums[1:]), linear(nums[:-1]))