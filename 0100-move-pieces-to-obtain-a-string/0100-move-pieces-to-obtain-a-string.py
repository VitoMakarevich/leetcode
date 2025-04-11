class Solution:
    def canChange(self, start: str, target: str) -> bool:
      start_i = 0
      target_i = 0

      start = start + '_'
      target = target + '_'
      # False if next at start and target is different
      # if 'R' at start is bigger than at target
      # if 'L' at start is smaller than at target
      while start_i < len(start) and target_i < len(start):
        while start_i < len(start) and start[start_i] == '_':
          start_i += 1
        while target_i < len(target) and target[target_i] == '_':
          target_i += 1
        if start_i < len(start) and target_i < len(start):
          if (start[start_i] != target[target_i]
            or (start[start_i] == 'L' and start_i < target_i)
            or (start[start_i] == 'R' and start_i > target_i)):
            return False
          start_i += 1
          target_i += 1

      return start_i == len(target) and len(target) == target_i