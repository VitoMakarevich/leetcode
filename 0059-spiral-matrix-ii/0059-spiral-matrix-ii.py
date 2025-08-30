class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
      directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
      
      min_row, max_row, min_col, max_col = 0, n, 0, n

      row = 0
      col = 0
      cur_dir = 0
      res = [[0] * n for _ in range(n)]
      cur = 1

      while cur <= n * n:
        if cur_dir == 0:
          while col < max_col:
            res[row][col] = cur
            cur += 1
            col += 1
          col -= 1
          row += 1
          min_row += 1
        elif cur_dir == 1:
          while row < max_row:
            res[row][col] = cur
            cur += 1
            row += 1
          row -= 1
          col -= 1
          max_col -= 1
        elif cur_dir == 2:
          while col >= min_col:
            res[row][col] = cur
            cur += 1
            col -= 1
          col += 1
          row -= 1
          max_row -= 1
        else:
          while row >= min_row:
            res[row][col] = cur
            cur += 1
            row -= 1
          row += 1
          col += 1
          min_col += 1
        cur_dir = (cur_dir + 1) % 4
      return res