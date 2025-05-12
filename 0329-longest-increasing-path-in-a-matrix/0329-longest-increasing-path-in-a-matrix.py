class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
      rows = len(matrix)
      cols = len(matrix[0])
      res = 0
      @cache
      def dp(i, j):
        cur = matrix[i][j]
        res = 0

        for nx, ny in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
          if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > cur:
            res = max(res, dp(nx, ny))
        return res + 1
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          res = max(res, dp(i, j))
      
      return res