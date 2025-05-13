class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [(0, (0, 0))]
        visited = set()
        rows, cols = len(heights), len(heights[0])
        prices = [[inf] * cols for _ in range(rows)]
        prices[0][0] = 0

        target = (rows - 1, cols - 1)
        while pq:
          price, pos = heapq.heappop(pq)
          i, j = pos
          if pos == target:
            return price
          if pos in visited:
            continue
          visited.add(pos)
          for nx, ny in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= nx < rows and 0 <= ny < cols:
              jump_price = abs(heights[i][j] - heights[nx][ny])
              potential_price = max(price, jump_price)
              if potential_price <= prices[nx][ny]:
                prices[nx][ny] = potential_price
                heapq.heappush(pq, (potential_price, (nx, ny)))
        

          