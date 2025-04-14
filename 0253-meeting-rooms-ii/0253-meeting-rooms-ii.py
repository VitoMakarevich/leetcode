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
          while pq and pq[0] <= interval[1]:
            heapq.heappop(pq)
          heapq.heappush(pq, interval[1])
        max_used = max(max_used, len(pq))
      return max_used
        # intervals.sort()
        # events = SortedDict(int)
        # change_times = set()
        # for start, end in intervals:
        #     events[start] = events.get(start, 0) + 1
        #     events[end] = events.get(end, 0) - 1
        # current_rooms = 0
        # max_rooms_in_use = 0
        # for time, change in events.items():
        #     current_rooms += change
        #     max_rooms_in_use = max(max_rooms_in_use, current_rooms)
        # return max_rooms_in_use
