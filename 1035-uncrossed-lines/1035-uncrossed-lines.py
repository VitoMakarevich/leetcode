class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
       self._m = len(nums1)
       self._n = len(nums2)
       self._nums1 = nums1
       self._nums2 = nums2

       return self._solve(0, 0, {})
    
    def _solve(self, left_pos, right_pos, cache):
      if left_pos == self._m or right_pos == self._n:
        return 0
      cache_key = f"{left_pos}-{right_pos}"
      if not cache_key in cache:
        if self._nums1[left_pos] == self._nums2[right_pos]:
          cache[cache_key] = 1 + self._solve(left_pos + 1, right_pos + 1, cache)
        else:
          cache[cache_key] = max([self._solve(left_pos + 1, right_pos, cache), self._solve(left_pos, right_pos + 1, cache)])
      return cache[cache_key]