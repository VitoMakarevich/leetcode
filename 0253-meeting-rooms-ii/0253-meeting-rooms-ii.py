from functools import cmp_to_key

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pq = []
        res = 0
        for interval in intervals + [(100000000, 100000000)]:
          if len(pq) == 0 or pq[0] > interval[0]:
            heapq.heappush(pq, interval[1])
          else:
            res = max(len(pq), res)
            while pq and pq[0] <= interval[0]:
              heapq.heappop(pq)
            heapq.heappush(pq, interval[1])
        return res
