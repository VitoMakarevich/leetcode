class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      size = 0
      for j in range(len(grid[0])):
        for i in range(len(grid)):
          if grid[i][j] == 1:
            size = max(size, self._dfs(grid, (i, j)))
      return size

    def _dfs(self, grid, pos):
      size = 1
      i, j = pos
      grid[i][j] = 0
      for adj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        adj_i, adj_j = adj
        if adj_i >= 0 and adj_i < len(grid) and adj_j >= 0 and adj_j < len(grid[0]) and grid[adj_i][adj_j] == 1 :
          size += self._dfs(grid, adj)
      
      return size