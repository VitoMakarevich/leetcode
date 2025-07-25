class Solution:
    def maxSum(self, nums: List[int]) -> int:
        values = set()
        for n in nums:
          values.add(n)
        sum_positive = 0
        max_below_equal_zero = -inf
        for v in values:
          if v > 0:
            sum_positive += v
          if v <= 0:
            max_below_equal_zero = max(v, max_below_equal_zero)
        if sum_positive > 0:
          return sum_positive
        else:
          return max_below_equal_zero