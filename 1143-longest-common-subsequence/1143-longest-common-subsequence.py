class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      self.text1 = text1
      self.text2 = text2
      cache = {}
      return self.solve(0, 0, cache)

    def solve(self, p1, p2, cache):
      key = (p1, p2)
      if not key in cache:
        if p1 == len(self.text1) or p2 == len(self.text2):
          cache[key] = 0
        elif self.text1[p1] == self.text2[p2]:
          cache[key] = 1 + self.solve(p1 + 1, p2 + 1, cache)
        else:
          cache[key] = max(self.solve(p1 + 1, p2, cache), self.solve(p1, p2 + 1, cache))
      return cache[key]
