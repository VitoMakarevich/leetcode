class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        total_size = len(grid) * len(grid[0])
        visited = set()
        for i in range(len(grid)):
          if grid[i][0] == 1:
            self._dfs((i, 0), visited, len(grid), len(grid[0]), grid)
          if grid[i][len(grid[0]) - 1] == 1:
            self._dfs((i, len(grid[0]) - 1), visited, len(grid), len(grid[0]), grid)
        for j in range(len(grid[0])):
          if grid[0][j] == 1:
            self._dfs((0, j), visited, len(grid), len(grid[0]), grid)
          if grid[len(grid) - 1][j] == 1:
            self._dfs((len(grid) - 1, j), visited, len(grid), len(grid[0]), grid)
        return sum(sum(row) for row in grid)
        
    def _dfs(self, coord, visited, rows, cols, grid):
      grid[coord[0]][coord[1]] = 0
      for direction in self.get_valid_directions(coord[0], coord[1], rows, cols):
        if grid[direction[0]][direction[1]] == 1:
          self._dfs(direction, visited, rows, cols, grid)

    def get_valid_directions(self, x, y, rows, cols):
      valid_directions = []
      
      for dx, dy in self.directions:
          nx, ny = x + dx, y + dy
          if 0 <= nx < rows and 0 <= ny < cols:
              valid_directions.append((nx, ny))
      
      return valid_directions