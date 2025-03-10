class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        return self._dp(0)

    @cache
    def _dp(self, pos):
      if pos >= len(self.s):
        return 1
      cur = int(self.s[pos])
      if cur == 0:
        return 0
      if 1 <= cur <= 2 and pos + 1 < len(self.s) and (cur == 1 or (cur == 2 and 1 <= int(self.s[pos + 1]) <= 6)):
        return self._dp(pos + 1) + self._dp(pos + 2)
      if pos + 1 < len(self.s) and self.s[pos + 1] == '0':
        if cur * 10 + int(self.s[pos + 1]) <= 26:
          return self._dp(pos + 2)
        else:
          return 0
      return self._dp(pos + 1)
      