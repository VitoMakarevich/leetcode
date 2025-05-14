import queue 
from functools import cmp_to_key
import heapq
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key = lambda x: x[1])
        ans = 1
        last_popped_y = points[0][1]
        for x, y in points[1:]:
          if x <= last_popped_y:
            continue
          else:
            last_popped_y = y
            ans += 1
        return ans