class Solution:
    def numTilings(self, n: int) -> int:
      if n <= 2:
        return n
      fully_covered = [0] * (n + 1)
      partially_covered = [0] * (n + 1)
      fully_covered[1] = 1
      fully_covered[2] = 2

      partially_covered[2] = 1
      for k in range(3, n + 1):
        fully_covered[k] = (fully_covered[k - 2] + fully_covered[k - 1] + 2 * partially_covered[k - 1]) % 1_000_000_007
        partially_covered[k] = (fully_covered[k - 2] + partially_covered[k - 1]) % 1_000_000_007
      return fully_covered[n]
