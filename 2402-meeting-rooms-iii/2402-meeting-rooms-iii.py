class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        usage = defaultdict(int)
        waiting = deque()
        meetings.sort()
        running = []
        free_rooms = [i for i in range(n)]
        for start, end in meetings:
          end_time = None
          while len(running) and start >= running[0][0]:
            end_time, room = heapq.heappop(running)
            heapq.heappush(free_rooms, room)
          if free_rooms:
            room = heapq.heappop(free_rooms)
            usage[room] += 1
            heapq.heappush(running, (end, room))

          else:
            next_end, room = heapq.heappop(running)
            duration = end - start
            usage[room] += 1
            heapq.heappush(running, (duration + next_end, room))
        max_room_usage = 0
        res_room = 0
        for room in range(n):
          used = usage[room]
          if used > max_room_usage:
            res_room = room
            max_room_usage = used
        return res_room