class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
      visited = set()
      for fb in forbidden:
        visited.add((fb, False))
        visited.add((fb, True))
      q = deque([(0, False)])
      steps = 0
      max_possible_to_jump_to_target = max(x, max(forbidden, default=0)) + a + b + 2000
      while q:
        
        for _ in range(len(q)):
          cur, is_from_backward = q.popleft()
          if cur == x:
            return steps
          
          if cur > max_possible_to_jump_to_target:
            pass
          elif is_from_backward:
            next_state = (cur + a, False)
            if not next_state in visited:
              q.append(next_state)
              visited.add(next_state)
          else:
            to_right = (cur + a, False)
            if not to_right in visited:
              q.append(to_right)
              visited.add(to_right)
            if cur - b >= 0:
              to_left = (cur - b, True)
              if not to_left in visited:
                q.append(to_left)
                visited.add(to_left)
        steps += 1

      return -1