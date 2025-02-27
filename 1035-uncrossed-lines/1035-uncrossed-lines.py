class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
       self._m = len(nums1)
       self._n = len(nums2)
       self._nums1 = nums1
       self._nums2 = nums2

       return self._solve(0, 0)
    @cache
    def _solve(self, left_pos, right_pos):
      cand = []
      for l in range(left_pos, self._m):
        for r in range(right_pos, self._n):
          if self._nums1[l] == self._nums2[r]:
            cand.append(self._solve(l + 1, r + 1))
      if len(cand) > 0:
        return 1 + max(cand)
      
      return 0