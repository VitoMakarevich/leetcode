class Solution:
    def minInsertions(self, s: str) -> int:
      return self._internal(s, {})

    def _internal(self, str, cache):
      if len(str) == 1 or len(str) == 0:
        return 0
      if str in cache:
        return cache[str]
      else:
        if str[0] == str[-1]:
          cache[str] = self._internal(str[1:-1], cache)
        else:
          cache[str] = 1 + min(self._internal(str[1:], cache), self._internal(str[:-1], cache))
      return cache[str]