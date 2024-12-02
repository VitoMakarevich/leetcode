class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_val = float('-inf')
        max_idx = -1

        min_val = float('inf')
        min_idx = -1

        for index, value in enumerate(nums):
          if value >= max_val:
            max_val = value
            max_idx = index
          if value < min_val:
            min_val = value
            min_idx = index
        cnt = 0
        if min_idx > max_idx:
          cnt -= 1
        cnt += min_idx + len(nums) - 1 - max_idx
        return cnt
