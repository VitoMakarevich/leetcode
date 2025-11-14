class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
      res = [[0] * n for _ in range(n)]
      sweep = [[0] * n for _ in range(n)]
      for lt_i, lt_j, rb_i, rb_j in queries:

        for row in range(lt_i, rb_i + 1):
          sweep[row][lt_j] += 1
          if rb_j + 1 < n:
            sweep[row][rb_j + 1] -= 1
      
      for row in range(n):
        cur = 0
        for col in range(n):
          cur += sweep[row][col]
          res[row][col] = cur
      return res
