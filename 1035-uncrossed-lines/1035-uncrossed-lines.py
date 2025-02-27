class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
       self._m = len(nums1)
       self._n = len(nums2)
       self._nums1 = nums1
       self._nums2 = nums2

       return self._solve(0, 0, {})
    
    def _solve(self, left_pos, right_pos, cache):
      cache_key = f"{left_pos}-{right_pos}"
      if not cache_key in cache:
        cand = []
        for l in range(left_pos, self._m):
          for r in range(right_pos, self._n):
            if self._nums1[l] == self._nums2[r]:
              cand.append(self._solve(l + 1, r + 1, cache))
        if len(cand) > 0:
          cache[cache_key] = 1 + max(cand)
        else:
          cache[cache_key] = 0
      return cache[cache_key]