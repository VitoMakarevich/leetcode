class Solution:
    def numSub(self, s: str) -> int:
      res = 0
      i = 0
      s += '0'
      mod = (10 ** 9 + 7)
      @cache
      def count(l):
        return ((1 + length) / 2 * length) % mod
      while i < len(s):
        if s[i] == '1':
          start = i
          while i < len(s) and s[i] == '1':
            i += 1
          i -= 1
          length = i - start + 1
          res += count(length)
        i += 1
      return int(res)
        

        