class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
      islands = 0
      rows = len(grid)
      cols = len(grid[0])
      for i in range(rows):
        if grid[i][0] == 0:
          self._dfs(i, 0, grid, rows, cols)
        if grid[i][cols - 1] == 0:
          self._dfs(i, cols - 1, grid, rows, cols)
      for j in range(cols):
        if grid[0][j] == 0:
          self._dfs(0, j, grid, rows, cols)
        if grid[rows - 1][j] == 0:
          self._dfs(rows - 1, j, grid, rows, cols)
      for i in range(rows):
        for j in range(cols):
          if grid[i][j] == 0 and (i != 0 and i != rows - 1 and j != 0 and j != cols - 1):
            self._dfs(i, j, grid, rows, cols)
            islands += 1
      return islands

        
    def _dfs(self, x, y, grid, rows, cols):
      grid[x][y] = 1
      for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if nx >= 0 and nx < rows and ny >= 0 and ny < cols and grid[nx][ny] == 0:
          self._dfs(nx, ny, grid, rows, cols)
      
