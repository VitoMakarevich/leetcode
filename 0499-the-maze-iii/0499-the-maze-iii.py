class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        start_tuple = (ball[1], ball[0])
        visited = set()
        visited.add(start_tuple)
        target = (hole[1], hole[0])
        width = len(maze[0])
        height = len(maze)
        q = [self._calculate_item(start_tuple, target, 0, "")]
        while q:
          score, rest = heapq.heappop(q)
          
          distance, current, path = rest
          visited.add(current)
          if current == target:
            return path
          for neigh, new_distance, direction in self._get_new_positions(current, maze, width, height, target):
            if not neigh in visited:
              heapq.heappush(q, self._calculate_item(neigh, target, new_distance + distance, path + direction))
        return "impossible"
          
    def _get_new_positions(self, current, maze, width, height, target):
      options = []
      for incr, direction in [((0, -1), 'u'), ((0, 1), 'd'), ((-1, 0), 'l'), ((1, 0), 'r')]:
        current_x, current_y = current
        nc = current
        while nc[0] >= 0 and nc[0] < width and nc[1] >= 0 and nc[1] < height and maze[nc[1]][nc[0]] == 0:
          if target == nc:
            break
          new = (nc[0] + incr[0], nc[1] + incr[1])
          if new[0] >= 0 and new[0] < width and new[1] >= 0 and new[1] < height and maze[new[1]][new[0]] == 0:
            nc = new
          else:
            break
        options.append((nc, abs(nc[0] - current[0]) + abs(nc[1] - current[1]), direction))
      return options

    def _calculate_item(self, current, target, distance, path):
      diff = sqrt(abs(target[0] - current[0]) ** 2 + abs(target[1] - current[1]) ** 2)
      return (diff + distance, (distance, current, path))
