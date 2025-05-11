class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        total_sum = sum([sum(r) for r in grid])
        if total_sum % 2 == 1:
          return False
        target = total_sum / 2
        def _s(matrix):
          s = 0
          for row in matrix:
            s += sum(row)
            if s == target:
              return True
            if s > target:
              break
          return False
        return _s(grid) or _s(zip(*grid))
        # rows, cols = len(grid), len(grid[0])
        # prefix_sum = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        # total_sum = 0
        # for i in range(1, len(grid) + 1):
        #   for j in range(1, len(grid[0]) + 1):
        #     prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + grid[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
        #     if prefix_sum[i][j] == target and (i == rows or j == cols):
        #       return True
        # return False