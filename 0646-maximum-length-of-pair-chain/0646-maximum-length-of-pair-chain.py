class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
      pairs.sort(key = lambda x: x[1])
      cur = float('-inf')
      res = 0
      for p in pairs:
        if p[0] > cur:
          res += 1
          cur = p[1]
      return res
      