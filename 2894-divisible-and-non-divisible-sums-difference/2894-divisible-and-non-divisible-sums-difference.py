class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = ((1 + n) * n) // 2
        other_count = n // m
        other_s = 0
        if other_count == 1:
          other_s = m
        elif other_count > 1:
          other_s = (m + other_count * m) * other_count // 2
        return s - 2 * other_s