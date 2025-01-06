from functools import cmp_to_key

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=cmp_to_key(Solution.compare))
        pq = []
        res = 0
        for interval in intervals + [(float('inf'), float('inf'))]:
          if len(pq) == 0 or pq[0] > interval[0]:
            heapq.heappush(pq, interval[1])
          else:
            if pq[0] <= interval[0]:
              res = max(len(pq), res)
              while pq and pq[0] <= interval[0]:
                heapq.heappop(pq)
              heapq.heappush(pq, interval[1])
        return res

    @staticmethod
    def compare(left, right):
      if left[0] < right[0]:
        return -1
      elif left[1] > right[1]:
        return 1
      else:
        if right[0] < right[1]:
          return 1
        elif right[0] > right[1]:
          return -1
        return 0
      