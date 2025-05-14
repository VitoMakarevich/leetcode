class Solution:
    def jump(self, nums: List[int]) -> int:
      last_idx = len(nums) - 1
      
      @cache
      def dp(start_idx):
        if start_idx >= last_idx:
          return 0
        min_jumps_to_reach = inf
        for jump_range in range(1, nums[start_idx] + 1):
          min_jumps_to_reach = min(dp(jump_range + start_idx), min_jumps_to_reach)
        return 1 + min_jumps_to_reach

      return dp(0)