class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
      self._points = points
      self._rows = len(points)
      self._cols = len(points[0])
      return max(self._dp(0))
    @cache
    def _dp(self, row):
      if row == self._rows:
        return [0] * self._cols
      next_dp = self._dp(row + 1)
      left_max = [next_dp[0]]
      for index in range(1, self._cols):
        left_max.append(max(left_max[index - 1] - 1, next_dp[index]))
      
      right_max = [0] * len(self._points[row])
      right_max[-1] = next_dp[-1]
      for index in range(self._cols - 2, -1, -1):
        right_max[index] = max(next_dp[index], right_max[index + 1] - 1)

      res = []
      for col in range(self._cols):
        res.append(self._points[row][col] + max(left_max[col], right_max[col]))
      return res