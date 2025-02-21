class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        start_tuple = (start[1], start[0])
        visited = set()
        visited.add(start_tuple)
        target = (destination[1], destination[0])
        width = len(maze[0])
        height = len(maze)
        q = [self._calculate_item(start_tuple, target, 0)]
        while q:
          score, rest = heapq.heappop(q)
          distance, current = rest
          if current[0] == destination[1] and current[1] == destination[0]:
            return distance
          for neigh, new_distance in self._get_new_positions(current, maze, width, height):
            if not neigh in visited:
              visited.add(current)
              heapq.heappush(q, self._calculate_item(neigh, target, new_distance + distance))
        return -1

          
    def _get_new_positions(self, current, maze, width, height):
      options = []
      #right
      current_x, current_y = current
      while current_x + 1 < width:
        if maze[current_y][current_x + 1] == 0:
          current_x += 1
        else:
          break
      options.append(((current_x, current_y), current_x - current[0]))
      #left
      current_x, current_y = current
      while current_x - 1 >= 0:
        if maze[current_y][current_x - 1] == 0:
          current_x -= 1
        else:
          break
      options.append(((current_x, current_y), current[0] - current_x))
      #bottom
      current_x, current_y = current
      while current_y + 1 < height:
        if maze[current_y + 1][current_x] == 0:
          current_y += 1
        else:
          break
      options.append(((current_x, current_y), current_y - current[1]))
      #up
      current_x, current_y = current
      while current_y - 1 >= 0:
        if maze[current_y - 1][current_x] == 0:
          current_y -= 1
        else:
          break
      options.append(((current_x, current_y), current[1] - current_y))
      return options


    def _calculate_item(self, current, target, distance):
      diff = sqrt(abs(target[0] - current[0]) ** 2 + abs(target[1] - current[1]) ** 2)
      return (diff + distance, (distance, current))
