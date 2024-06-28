import queue 
from functools import cmp_to_key
import heapq
class Solution:
    @staticmethod
    def custom_compare(o1):
      # For example, let's sort integers based on their absolute values
      return o1[0]
  
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        current_ends = []
        sorted_points = sorted(points, key=Solution.custom_compare)
        last_cut = float('-inf')
        for item in sorted_points:
          if len(current_ends) > 0 and current_ends[0] < item[0]:
            count += 1
            last_cut = current_ends[0]
            current_ends = [item[1]]

          heapq.heappush(current_ends, item[1])

        if current_ends[0] > last_cut:
          count += 1
        return count