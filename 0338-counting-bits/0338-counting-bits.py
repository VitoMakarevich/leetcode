class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for v in range(n + 1):
          count_ones = 0
          while v > 0:
            count_ones += int(1 & v)
            v >>= 1
          res.append(count_ones)
        return res