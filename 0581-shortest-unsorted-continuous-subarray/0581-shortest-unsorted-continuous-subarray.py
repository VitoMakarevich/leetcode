class Solution:
  def findUnsortedSubarray(self, a: List[int]) -> int:
        n = len(a)
        r, mx = -1, -1e6

        for i in range(n):
            if a[i] >= mx:
                mx = a[i]
            else:
                r = i

        l, mn = n, 1e6

        for i in range(n - 1, -1, -1):
            if a[i] <= mn:
                mn = a[i]
            else:
                l = i

        return max(0, r - l + 1)