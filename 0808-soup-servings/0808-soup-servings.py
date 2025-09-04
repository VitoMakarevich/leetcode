class Solution:
    
    def soupServings(self, n: int) -> float:
      n = ceil(n / 25)
      dp = {}
      decrements = [(4, 0), (3, 1), (2, 2), (1, 3)]
      

      def calc_dp(a, b):
        total_prob = 0
        for a_dec, b_dec in decrements:
          total_prob += dp[max(0, a - a_dec)][max(0, b - b_dec)]
        return total_prob / 4

      dp[0] = {0: 0.5}
      for k in range(1, n + 1):
        dp[0][k] = 1
        dp[k] = {0: 0}
        for j in range(1, k + 1):
          dp[j][k] = calc_dp(j, k)
          dp[k][j] = calc_dp(k, j)
        if dp[k][k] > 1 - 1e-5:
          return 1
      return dp[n][n]