class Solution:
    def numSub(self, s: str) -> int:
      res = 0
      i = 0
      s += '0'
      mod = (10 ** 9 + 7)
      groups = defaultdict(int)
      while i < len(s):
        if s[i] == '1':
          start = i
          while i < len(s) and s[i] == '1':
            i += 1
          i -= 1
          length = i - start + 1
          groups[length] += 1
        i += 1
      for size, count in groups.items():
        res += (count * ((1 + size) * size // 2)) % mod
      return res
        

        