class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      self._nums = nums
      memo = {}
      return self._dp(0, float('-inf'), memo)[1]
        
    def _dp(self, i: int, prev: int, memo) -> int:
        if i == len(self._nums):
          return 0, 1
        key = (i, prev)
        if not key in memo:
          taken_length = 0
          taken_count = 0
          with_this = 0
          if self._nums[i] > prev:
            taken_length, taken_count = self._dp(i + 1, self._nums[i], memo)
            taken_length += 1
          not_taken_length, not_taken_count = self._dp(i + 1, prev, memo)
          if taken_length > not_taken_length:
            memo[key] = taken_length, taken_count
          elif taken_length == not_taken_length:
            memo[key] = taken_length, taken_count + not_taken_count
          else:
            memo[key] = not_taken_length, not_taken_count
        return memo[key]