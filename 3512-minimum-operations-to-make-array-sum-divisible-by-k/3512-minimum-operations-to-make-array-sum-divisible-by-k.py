class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
      s = 0
      for c in nums:
        s = (s + c % k) % k
      return s