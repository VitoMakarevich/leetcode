class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, columns = len(grid), len(grid[0])
        total_size = rows * columns
        for i in range(rows):
          if grid[i][0] == 1:
            self._dfs((i, 0), rows, columns, grid)
          if grid[i][columns - 1] == 1:
            self._dfs((i, columns - 1), rows, columns, grid)
        for j in range(columns):
          if grid[0][j] == 1:
            self._dfs((0, j), rows, columns, grid)
          if grid[rows - 1][j] == 1:
            self._dfs((rows - 1, j), rows, columns, grid)
        return sum(sum(row) for row in grid)
        
    def _dfs(self, coord, rows, cols, grid):
      grid[coord[0]][coord[1]] = 0
      for direction in self.get_valid_directions(coord[0], coord[1], rows, cols):
        if grid[direction[0]][direction[1]] == 1:
          self._dfs(direction, rows, cols, grid)

    def get_valid_directions(self, x, y, rows, cols):
      valid_directions = []
      
      for dx, dy in self.directions:
          nx, ny = x + dx, y + dy
          if 0 <= nx < rows and 0 <= ny < cols:
              valid_directions.append((nx, ny))
      
      return valid_directions