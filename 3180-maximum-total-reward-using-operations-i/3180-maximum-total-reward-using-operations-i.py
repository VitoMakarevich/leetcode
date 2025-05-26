class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        values = set()
        for v in rewardValues:
          values.add(v)
        values = list(values)
        values.sort()
        @cache
        def dp(prev_sum):
          leftmost = bisect_right(values, prev_sum)
          if leftmost == len(values):
            return 0
          cand = 0
          for idx in range(leftmost, len(values)):
            cand = max(cand, values[idx] + dp(prev_sum + values[idx]))
          return cand
        return dp(0)