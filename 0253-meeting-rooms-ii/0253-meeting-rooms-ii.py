from sortedcontainers import SortedDict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      max_used = 0
      pq = []
      intervals.sort()
      for interval in intervals + [(100000000, 100000000)]:
        if not pq or pq[0] > interval[0]:
          heapq.heappush(pq, interval[1])
        else:
          while pq and pq[0] <= interval[0]:
            heapq.heappop(pq)
          heapq.heappush(pq, interval[1])
        max_used = max(max_used, len(pq)) 
       
      return max_used

