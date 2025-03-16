class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
      self.nums = nums
      r = self._dp(0, len(nums) - 1)
      return r >= 0
    
    @cache
    def _dp(self, i, j):
      if i == j:
        return self.nums[i]
      left = self._dp(i + 1, j)
      right = self._dp(i, j - 1)
      return max(self.nums[i] - left, self.nums[j] - right)
      