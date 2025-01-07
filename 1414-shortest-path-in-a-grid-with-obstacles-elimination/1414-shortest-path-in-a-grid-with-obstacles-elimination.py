class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
      init = ((0, 0), k)
      rows, cols = len(grid), len(grid[0])
      q = deque([init])
      visited = set()
      visited.add(init)
      turn = 0
      while q:
        for i in range(len(q)):
          cur_coordinates, obstacles = q.popleft()
          i, j = cur_coordinates
          if i == rows - 1 and j == cols - 1:
            return turn
          for neigh_i, neigh_j in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if neigh_i >= 0 and neigh_i < rows and neigh_j >= 0 and neigh_j < cols:
              if grid[neigh_i][neigh_j] == 1 and obstacles > 0:
                next_step = ((neigh_i, neigh_j), obstacles - 1)
                if not next_step in visited:
                  visited.add(next_step)
                  q.append(next_step)
              elif grid[neigh_i][neigh_j] == 0:
                next_step = ((neigh_i, neigh_j), obstacles)
                if not next_step in visited:
                  visited.add(next_step)
                  q.append(next_step)
        turn += 1
      return -1
          

