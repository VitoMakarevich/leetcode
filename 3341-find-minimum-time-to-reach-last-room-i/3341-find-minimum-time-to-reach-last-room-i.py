import heapq
from math import inf
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        rows = len(moveTime)
        cols = len(moveTime[0])
        distances = [[inf] * cols for _ in range(rows)]
        distances[0][0] = 0
        while pq:
          cur_time, x, y = heapq.heappop(pq)
          if cur_time > distances[y][x]:
            continue

          for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= ny < rows and 0 <= nx < cols:
              potential_distance = max(cur_time, moveTime[ny][nx]) + 1
              if potential_distance < distances[ny][nx]:
                distances[ny][nx] = potential_distance
                heapq.heappush(pq, (potential_distance, nx, ny))
        return distances[rows - 1][cols - 1]