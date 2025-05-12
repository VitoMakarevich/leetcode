class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      

      @cache
      def dp(pos, remain):
        if pos == len(nums):
          return int(remain == 0)
        if_subtract_cur = dp(pos + 1, remain - nums[pos])
        if_add_cur = dp(pos + 1, remain + nums[pos])
        return if_subtract_cur + if_add_cur

      return dp(0, target)