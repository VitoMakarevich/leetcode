class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = {}
        res = 1
        for v in arr:
          before = cache.get(v - difference, 0)
          res = max(1 + before, res)
          cache[v] = 1 + before
        return res