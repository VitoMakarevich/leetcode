class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        return self._proxy(0)

    def _proxy(self, v):
      r = self._dp(v)
      print(v, r)
      return r

    @cache
    def _dp(self, pos):
      if pos >= len(self.s):
        return 1
      cur = int(self.s[pos])
      if cur == 0:
        return 0
      if 1 <= cur <= 2 and pos + 1 < len(self.s) and (cur == 1 or (cur == 2 and 1 <= int(self.s[pos + 1]) <= 6)):
        return self._proxy(pos + 1) + self._proxy(pos + 2)
      if pos + 1 < len(self.s) and self.s[pos + 1] == '0':
        return self._proxy(pos + 2)
      return self._proxy(pos + 1)
      