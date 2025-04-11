class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
          return False
        rightmost_set_bit = n & (-n)
        return n & (-n) == n