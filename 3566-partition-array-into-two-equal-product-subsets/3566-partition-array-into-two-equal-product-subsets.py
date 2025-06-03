class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
      total_product = 1
      for n in nums:
        total_product *= n
      if sqrt(total_product) != target:
        return False
      @cache
      def dp(idx, new_target):
        if new_target == 1:
          return True
        if idx == len(nums):
          return False
        return dp(idx + 1, new_target) or dp(idx + 1, new_target / nums[idx])
      return dp(0, target)