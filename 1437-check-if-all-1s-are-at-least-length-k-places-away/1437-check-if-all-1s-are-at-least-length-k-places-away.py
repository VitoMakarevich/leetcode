class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
      prev_position = float('-inf')
      for idx, c in enumerate(nums):
        if c == 1:
          if idx - prev_position <= k:
            return False
          prev_position = idx
      return True