class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, columns = len(grid), len(grid[0])
        total_size = rows * columns
        for i in range(rows):
          for j in range(columns):
            if grid[i][j] == 1 and (i == 0 or j == 0 or i == rows - 1 or j == columns - 1):
              self._dfs((i, j), rows, columns, grid)
        return sum(sum(row) for row in grid)
        
    def _dfs(self, coord, rows, cols, grid):
      grid[coord[0]][coord[1]] = 0
      i, j = coord
      for direction in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
        if 0 <= direction[0] < rows and 0 <= direction[1] < cols and grid[direction[0]][direction[1]]:
          self._dfs(direction, rows, cols, grid)