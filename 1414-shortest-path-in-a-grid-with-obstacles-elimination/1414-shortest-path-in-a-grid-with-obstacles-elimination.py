class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
      init = (0, 0, k)
      rows, cols = len(grid), len(grid[0])
      q = deque([init])
      visited = set()
      visited.add(init)
      turn = 0
      while q:
        for i in range(len(q)):
          i, j, obstacles = q.popleft()
          if i == rows - 1 and j == cols - 1:
            return turn
          for neigh_i, neigh_j in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if neigh_i >= 0 and neigh_i < rows and neigh_j >= 0 and neigh_j < cols and not (neigh_i, neigh_j, obstacles) in visited:
              if grid[neigh_i][neigh_j] == 1 and obstacles > 0:
                visited.add((neigh_i, neigh_j, obstacles))
                q.append((neigh_i, neigh_j, obstacles - 1))
              elif grid[neigh_i][neigh_j] == 0:
                next_step = (neigh_i, neigh_j, obstacles)
                visited.add(next_step)
                q.append(next_step)
        turn += 1
      return -1
          

