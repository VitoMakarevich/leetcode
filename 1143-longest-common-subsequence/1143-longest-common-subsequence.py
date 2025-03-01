class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      self.text1 = text1
      self.text2 = text2
      return self.solve(0, 0)
    @cache
    def solve(self, p1, p2):
      if p1 == len(self.text1) or p2 == len(self.text2):
        return 0
      if self.text1[p1] == self.text2[p2]:
        return 1 + self.solve(p1 + 1, p2 + 1)
      else:
        return max(self.solve(p1 + 1, p2), self.solve(p1, p2 + 1))
