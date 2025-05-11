class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        prefix_sum = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        total_sum = 0
        for i in range(1, len(grid) + 1):
          for j in range(1, len(grid) + 1):
            total_sum += grid[i - 1][j - 1]
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + grid[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
        
        low, high = 0, rows - 1

        while low <= high:
          mid = (low + high) // 2
          one_part_sum = prefix_sum[mid][cols]
          second_part_sum = total_sum - one_part_sum
          if one_part_sum == second_part_sum:
            return True
          elif one_part_sum < second_part_sum:
            low = mid + 1
          else:
            high = mid - 1

        low, high = 0, cols - 1

        while low <= high:
          mid = (low + high) // 2
          one_part_sum = prefix_sum[rows][mid]
          second_part_sum = total_sum - one_part_sum
          if one_part_sum == second_part_sum:
            return True
          elif one_part_sum < second_part_sum:
            low = mid + 1
          else:
            high = mid - 1
        
        
        return False