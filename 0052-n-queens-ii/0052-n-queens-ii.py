class State:
  def __init__(self):
    self.cols = set()
    self.diagonals_n = set()
    self.diagonals_r = set()

class Solution:
    def totalNQueens(self, n: int) -> int:
      res = [0]
      storage = State()
      self.backtrack(0, res, storage, n)
      return res[0]
    
    def backtrack(self, row, res, storage, n):
      if row == n:
        res[0] += 1
        return
      
      for column in range(n):
        n_diag = row - column
        r_diag = row + column
        if not column in storage.cols and not n_diag in storage.diagonals_n and not r_diag in storage.diagonals_r:
          storage.diagonals_n.add(n_diag)
          storage.diagonals_r.add(r_diag)
          storage.cols.add(column)
          self.backtrack(row + 1, res, storage, n)
          storage.diagonals_n.discard(n_diag)
          storage.diagonals_r.discard(r_diag)
          storage.cols.discard(column)