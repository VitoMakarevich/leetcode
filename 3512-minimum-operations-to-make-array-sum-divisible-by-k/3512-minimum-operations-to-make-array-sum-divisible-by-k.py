class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
      ar_sum = sum(nums)
      mod = ar_sum % k
      return mod