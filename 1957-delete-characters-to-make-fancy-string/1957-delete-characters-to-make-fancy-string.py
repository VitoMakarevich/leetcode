class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
          return s
        res = s[:2]
        first = s[0]
        second = s[1]
        for idx in range(2, len(s)):
          if s[idx] == first == second:
            continue
          res += s[idx]
          first, second = second, s[idx]
        return res