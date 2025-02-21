class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        target = (destination[0], destination[1])
        width = len(maze[0])
        height = len(maze)
        q = [self._calculate_item((start[0], start[1]), target, 0)]
        while q:
          score, rest = heapq.heappop(q)
          distance, current = rest
          visited.add(current)
          if current == target:
            return distance
          for neigh, new_distance in self._get_new_positions(current, maze, width, height):
            if not neigh in visited:
              visited.add(neigh)
              heapq.heappush(q, self._calculate_item(neigh, target, new_distance + distance))
        return -1

          
    def _get_new_positions(self, current, maze, width, height):
      options = []
      current_x, current_y = current
      while current_x + 1 < width and maze[current_x + 1][current_y] == 0:
        current_x += 1
      options.append(((current_x, current_y), current_x - current[0]))
      current_x, current_y = current
      while current_x - 1 >= 0 and maze[current_x - 1][current_y] == 0:
        current_x -= 1
      options.append(((current_x, current_y), current[0] - current_x))
      current_x, current_y = current
      while current_y + 1 < height and maze[current_x][current_y + 1] == 0:
        current_y += 1
      options.append(((current_x, current_y), current_y - current[1]))
      current_x, current_y = current
      while current_y - 1 >= 0 and maze[current_x][current_y - 1] == 0:
        current_y -= 1
      options.append(((current_x, current_y), current[1] - current_y))
      return options


    def _calculate_item(self, current, target, distance):
      diff = abs(target[0] - current[0]) + abs(target[1] - current[1])
      return (diff + distance, (distance, current))
