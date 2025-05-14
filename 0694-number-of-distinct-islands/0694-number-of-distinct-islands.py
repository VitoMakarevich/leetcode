class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = defaultdict(int)

        def dp(cur_pos, start, cur_island):
          visited.add(cur_pos)
          normalized_pos = (cur_pos[0] - start[0], cur_pos[1] - start[1])
          cur_island.add(normalized_pos)
          x, y = cur_pos
          for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= nx < rows and 0 <= ny < cols and not (nx, ny) in visited and grid[nx][ny] == 1:
              dp((nx, ny), start, cur_island)

        for i in range(rows):
          for j in range(cols):
            if grid[i][j] == 1 and not (i, j) in visited:
              shape = set()
              dp((i, j), (i, j), shape)
              islands[frozenset(shape)] += 1
        return len(islands)