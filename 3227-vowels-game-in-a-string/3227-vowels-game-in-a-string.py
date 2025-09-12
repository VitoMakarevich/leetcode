class Solution:
    def doesAliceWin(self, s: str) -> bool:
      vw = set(['a', 'e', 'i', 'o', 'u'])
      vw_count = 0
      for c in s:
        vw_count += int(c in vw)
      return vw_count > 0