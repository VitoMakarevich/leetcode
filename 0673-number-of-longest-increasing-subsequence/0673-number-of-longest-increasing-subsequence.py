class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      self._nums = nums
      return self._dp(0, float('-inf'))[1]
        
    @cache
    def _dp(self, i: int, prev: int) -> int:
        if i == len(self._nums):
          return 0, 1
        
        taken_length = 0
        taken_count = 0
        with_this = 0
        if self._nums[i] > prev:
          taken_length, taken_count = self._dp(i + 1, self._nums[i])
          taken_length += 1
        not_taken_length, not_taken_count = self._dp(i + 1, prev)
        if taken_length > not_taken_length:
          return taken_length, taken_count
        elif taken_length == not_taken_length:
          return taken_length, taken_count + not_taken_count
        else:
          return not_taken_length, not_taken_count