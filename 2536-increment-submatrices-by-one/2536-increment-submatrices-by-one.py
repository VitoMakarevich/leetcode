class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
      res = [[0] * (n) for _ in range(n)]
      sweep = [[0] * (n + 1) for _ in range(n + 1)]
      for lt_i, lt_j, rb_i, rb_j in queries:
        sweep[lt_i][lt_j] += 1
        sweep[rb_i + 1][rb_j + 1] += 1 
        if rb_i + 1 < n:
          sweep[rb_i + 1][lt_j] -= 1
        if rb_j + 1 < n:
          sweep[lt_i][rb_j + 1] -= 1

      
      print(sweep)
      for row in range(n):
        for col in range(n):
          top = 0 if row == 0 else res[row - 1][col]
          left = 0 if col == 0 else res[row][col - 1]
          top_left = 0 if col == 0 or row == 0 else res[row - 1][col - 1]
          res[row][col] = sweep[row][col] + top + left - top_left
      return res