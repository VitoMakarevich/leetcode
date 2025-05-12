class Solution:
    def countSubstrings(self, s: str) -> int:
      res = 0

      # logic:
      # if left == right:
      # add to res and return True
      # if left > right:
      # return True as border check will done on caller side - not add to res
      # if border values equal and dp - inner is True - add to res
      # call for (i + 1, j), (i, j - 1)
      @cache
      def dp(i, j):
        nonlocal res
        if i == j:
          res += 1
          return True
        if i > j:
          return True
        dp(i + 1, j)
        dp(i, j - 1)
        if s[i] == s[j] and dp(i + 1, j - 1):
          res += 1
          return True
        return False
        
      dp(0, len(s) - 1)
      return res