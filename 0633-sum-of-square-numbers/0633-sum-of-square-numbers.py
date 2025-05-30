class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, ceil(sqrt(c))
        while start <= end:
          cand = start ** 2 + end ** 2
          if cand == c:
            return True
          elif cand > c:
            end -= 1
          else:
            start += 1
        return False