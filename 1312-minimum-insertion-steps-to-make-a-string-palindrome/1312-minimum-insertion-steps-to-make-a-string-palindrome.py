class Solution:
    def minInsertions(self, s: str) -> int:
      return self._internal(s, 0, len(s) - 1,  {})

    def _internal(self, str, left, right, cache):
      if left >= right:
        return 0
      v = (left, right)
      if v in cache:
        return cache[v]
      else:
        print(left, right)
        if str[right] == str[left]:
          cache[v] = self._internal(str, left + 1, right - 1, cache)
        else:
          cache[v] = 1 + min(self._internal(str, left + 1, right, cache), self._internal(str, left, right - 1, cache))
      return cache[v]