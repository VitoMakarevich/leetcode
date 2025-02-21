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
      for (dx, dy), direction in [((0, -1), 'u'), ((0, 1), 'd'), ((-1, 0), 'l'), ((1, 0), 'r')]:
        nc = list(current)
        while True:
            new_x, new_y = nc[0] + dx, nc[1] + dy
            if not (0 <= new_x < width and 0 <= new_y < height) or maze[new_y][new_x] != 0:
                break
            nc = [new_x, new_y]  
            if target == tuple(nc):
                break
        options.append((tuple(nc), abs(nc[0] - current[0]) + abs(nc[1] - current[1]), direction))

      return options

    def _calculate_item(self, current, target, distance, path):
      diff = sqrt(abs(target[0] - current[0]) ** 2 + abs(target[1] - current[1]) ** 2)
      return (diff + distance, (distance, current, path))
