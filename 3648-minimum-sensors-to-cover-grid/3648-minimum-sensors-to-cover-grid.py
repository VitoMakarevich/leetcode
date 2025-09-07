class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
      horizontal_repetitions = ceil(m / (2 * k + 1))
      vertical_repetitions = ceil(n / (2 * k + 1))
      return horizontal_repetitions * vertical_repetitions
        