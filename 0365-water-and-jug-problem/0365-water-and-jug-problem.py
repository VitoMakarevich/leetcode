class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()
        q = deque([(0, 0)])
        while q:
          data = q.pop()
          cur_left, cur_right = data
          if cur_left + cur_right == target:
            return True
          if data in visited:
            continue
          visited.add(data)
          # 1
          q.append((x, 0))
          q.append((0, y))
          q.append((x, y))
          q.append((x, cur_right))
          q.append((cur_left, y))
          # 2
          q.append((cur_left, 0))
          q.append((0, cur_right))
          # 3
          # from left to right till left is empty
          if y - cur_right >= cur_left and y >= cur_left + cur_right:
            q.append((0, cur_right + cur_left))
          # from left to right till right is full
          if cur_left + cur_right >= y:
            q.append((cur_left - (y - cur_right) ,y))
          # from right to left till right is empty
          if x - cur_left >= cur_right and x >= cur_left + cur_right:
            q.append((cur_left + cur_right, 0))
          # from right to left till left is full
          if cur_left + cur_right >= x:
            q.append((x, cur_right - (x - cur_left))) 
          
        return False
