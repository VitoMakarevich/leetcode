class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
      res = 0
      abs_n = [abs(n) for n in nums]
      abs_n.sort()
      i = 0
      j = 1
      while i < len(nums):
        while j < len(nums) and abs_n[j] <= abs_n[i] * 2:
          j += 1
        res += j - i - 1
        i += 1
      return res