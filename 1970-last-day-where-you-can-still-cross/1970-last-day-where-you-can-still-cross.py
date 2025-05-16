class UF:
  def __init__(self, size):
    self._parent = [i for i in range(size)]
    self._count = [1 for _ in range(size)]
  def find(self, x):
    if self._parent[x] != x:
      self._parent[x] = self.find(self._parent[x])
    return self._parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if self._count[root_x] < self._count[root_y]:
      root_x, root_y = root_y, root_x
    self._parent[root_y] = root_x
    self._count[root_x] += self._count[root_y]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    # UF
    # custom indexing
    # coordinate translation  
      uf = UF(row * col + 2)
      left = 0
      self.row = row
      right = row * col + 1
      print(uf.find(left), uf.find(right))
      for i in range(row):
        uf.union(left, self.two_dim_to_one_dim(i, 0))
        uf.union(right, self.two_dim_to_one_dim(i, col - 1))
      print(uf.find(left), uf.find(right))
      matrix = [[0] * col for _ in range(row)]
      for idx, (affected_row, affected_col) in enumerate(cells, start = 1):
        affected_row -= 1
        affected_col -= 1
        matrix[affected_row][affected_col] = 1
        for nx, ny in [
          (affected_row - 1, affected_col),
          (affected_row + 1, affected_col),
          (affected_row, affected_col - 1),
          (affected_row, affected_col + 1),
          (affected_row - 1, affected_col - 1),
          (affected_row + 1, affected_col + 1),
          (affected_row + 1, affected_col - 1),
          (affected_row - 1, affected_col + 1),
        ]:
          if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 1:
            uf.union(self.two_dim_to_one_dim(nx, ny), self.two_dim_to_one_dim(affected_row, affected_col))
        if uf.find(left) == uf.find(right):
          return idx - 1

    def two_dim_to_one_dim(self, x, y):
      return x * self.row + y + 1
    
