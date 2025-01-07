class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
      init = ((0, 0), k)
      rows, cols = len(grid), len(grid[0])
      q = [self.create_item(0, 0, k, 0, rows, cols)]
      visited = set()
      visited.add(init)
      res = float('inf')
      while q:
        distance, rest = heapq.heappop(q)
        i, j, turn, obstacles = rest
        if i == rows - 1 and j == cols - 1:
          return turn
        for neigh_i, neigh_j in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
          if neigh_i >= 0 and neigh_i < rows and neigh_j >= 0 and neigh_j < cols:
            if grid[neigh_i][neigh_j] == 1 and obstacles > 0:
              next_step = ((neigh_i, neigh_j), obstacles - 1)
              if not next_step in visited:
                visited.add(next_step)
                heapq.heappush(q, self.create_item(neigh_i, neigh_j, obstacles - 1, turn + 1, rows, cols))
            elif grid[neigh_i][neigh_j] == 0:
              next_step = ((neigh_i, neigh_j), obstacles)
              if not next_step in visited:
                visited.add(next_step)
                q.append(self.create_item(neigh_i, neigh_j, obstacles, turn + 1, rows, cols))
      return -1
    def create_item(self, i, j, obstacles, turn, rows, cols):
      distance = rows - 1 - i + cols - 1 - j + turn * turn - obstacles
      return (distance, (i, j, turn, obstacles))
          


