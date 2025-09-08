class Solution:
    def minOperations(self, s: str) -> int:
      smallest = inf
      all_chars = set(s)
      ordered = sorted(list(all_chars))
      if ordered[0] == 'a' and len(ordered) == 1:
        return 0
      elif ordered[0] == 'a':
        return 26 - (ord(ordered[1]) - ord('a'))
      else:
        return 26 - (ord(ordered[0]) - ord('a'))

      