class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      dp = [[0] * (n + 1) for _ in range(m + 1)]
      def zeros_ones(s):
        z = 0
        for c in s:
          z += int(c == '0')
        return z, len(s) - z
      for s in strs:
        zeros, ones = zeros_ones(s)
        for i in range(m, zeros - 1, -1):
          for j in range(n, ones - 1, -1):
            dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
      return dp[m][n]
