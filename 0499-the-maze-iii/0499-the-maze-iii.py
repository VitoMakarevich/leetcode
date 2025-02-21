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
      #right
      current_x, current_y = current
      while current_x + 1 < width:
        if target[0] == current_x and target[1] == current_y:
          break
        if maze[current_y][current_x + 1] == 0:
          current_x += 1
        else:
          break
      options.append(((current_x, current_y), current_x - current[0], "r"))
      #left
      current_x, current_y = current
      while current_x - 1 >= 0:
        if target[0] == current_x and target[1] == current_y:
          break
        if maze[current_y][current_x - 1] == 0:
          current_x -= 1
        else:
          break
      options.append(((current_x, current_y), current[0] - current_x, "l"))
      #bottom
      current_x, current_y = current
      while current_y + 1 < height:
        if target[0] == current_x and target[1] == current_y:
          break
        if maze[current_y + 1][current_x] == 0:
          current_y += 1
        else:
          break
      options.append(((current_x, current_y), current_y - current[1], "d"))
      #up
      current_x, current_y = current
      while current_y - 1 >= 0:
        if target[0] == current_x and target[1] == current_y:
          break
        if maze[current_y - 1][current_x] == 0:
          current_y -= 1
        else:
          break
      options.append(((current_x, current_y), current[1] - current_y, "u"))
      return options


    def _calculate_item(self, current, target, distance, path):
      diff = sqrt(abs(target[0] - current[0]) ** 2 + abs(target[1] - current[1]) ** 2)
      return (diff + distance, (distance, current, path))
