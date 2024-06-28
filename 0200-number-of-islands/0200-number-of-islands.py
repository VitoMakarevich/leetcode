class Solution:
    land = "1"
    sea = "0"
    visited = 3
    count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
      for y in range(len(grid)):
        for x in range(len(grid[y])):
          if grid[y][x] == self.land:
            self.count = self.count + 1
            self.dig_to(grid, x, y)
      return self.count

    def dig_to(self, grid, start_x, start_y):
      grid[start_y][start_x] = self.visited
      for x, y in self.adj(grid, start_x, start_y):
          self.dig_to(grid, x, y)
        
    def adj(self, grid, pos_x, pos_y) -> list[(int, int)]:
      res = []
      max_x = len(grid[0])
      max_y = len(grid)
      if pos_x - 1 >= 0 and grid[pos_y][pos_x - 1] == self.land:
        res.append((pos_x -1, pos_y))
      if pos_x + 1 < max_x and grid[pos_y][pos_x + 1] == self.land:
        res.append((pos_x + 1, pos_y))
      if pos_y - 1 >= 0 and grid[pos_y - 1][pos_x] == self.land:
        res.append((pos_x, pos_y - 1))
      if pos_y + 1 < max_y and grid[pos_y + 1][pos_x] == self.land:
        res.append((pos_x, pos_y + 1))
      return res
      