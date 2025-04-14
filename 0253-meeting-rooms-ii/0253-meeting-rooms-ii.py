from sortedcontainers import SortedDict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      max_used = 0
      pq = []
      intervals.sort(key = lambda x: x[0])
      for interval in intervals + [(100000000, 100000000)]:
        if not pq or pq[0] > interval[0]:
          heapq.heappush(pq, interval[1])
        else:
          max_used = max(max_used, len(pq)) 
          while pq and pq[0] <= interval[0]:
            heapq.heappop(pq)
          heapq.heappush(pq, interval[1])
        
       
      return max_used

