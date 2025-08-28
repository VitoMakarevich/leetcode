class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
      rows, cols = len(matrix), len(matrix[0])
      dp = [[0] * (cols + 1) for _ in range(rows + 1)]
      for row in range(rows):
        for col in range(cols):
          if matrix[row][col]:
            dp[row + 1][col + 1] = min(dp[row + 1][col], dp[row][col], dp[row][col + 1]) + matrix[row][col]
      return sum([sum(row) for row in dp])
