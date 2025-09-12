class Solution:
    def doesAliceWin(self, s: str) -> bool:
      vw = ['a', 'e', 'i', 'o', 'u']
      for v in vw:
        if s.find(v) != -1:
          return True
      return False