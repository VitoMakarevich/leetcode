class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        prefix_sum = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        total_sum = 0
        for i in range(1, len(grid) + 1):
          for j in range(1, len(grid[0]) + 1):
            total_sum += grid[i - 1][j - 1]
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + grid[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
        if not total_sum % 2 == 0:
          return False

        target = int(total_sum / 2)
        col_sum = prefix_sum[rows][1:]
        res = bisect_left(col_sum, target)
        if prefix_sum[rows][res + 1] == target:
          return True

        sum_vector_for_cols = []
        for i in range(len(grid)):
          sum_vector_for_cols.append(prefix_sum[i + 1][cols])
        
        res = bisect_left(sum_vector_for_cols, target)
        return prefix_sum[res + 1][cols] == target