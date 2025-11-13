class Solution:
    def maxOperations(self, s: str) -> int:
      res = 0
      level = 0
      idx = len(s) - 1
      while idx >= 0:
        if s[idx] == '0':
          level += 1
          while s[idx] == '0' and idx >= 0:
            idx -= 1
          if s[idx] == '1':
            idx += 1
        else:
          res += level
        idx -= 1
      return res