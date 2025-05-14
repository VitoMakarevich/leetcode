class Solution:
    def jump(self, nums: List[int]) -> int:
      cur_idx_end = cur_idx_biggest_jump = 0
      ans = 0
      idx = 0
      while idx < len(nums) - 1:
        cur_idx_end = idx + nums[idx]
        for i in range(idx + 1, cur_idx_end + 1):
          cur_idx_biggest_jump = max(cur_idx_biggest_jump, nums[i])
        idx += cur_idx_biggest_jump
        ans += 1


      return ans