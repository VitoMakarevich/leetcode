class UF:
  def __init__(self, size):
    self._parent = [i for i in range(size)]
    self._size = [1] * size

  def find(self, x):
    if self._parent[x] != x:
      self._parent[x] = self.find(self._parent[x])
    return self._parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x == root_y:
      return False
    if self._size[root_y] > self._size[root_x]:
      root_x, root_y = root_y, root_x
    self._parent[root_y] = root_x
    self._size[root_x] += self._size[root_y]
    return True

class Solution:
    

    def swimInWater(self, grid: List[List[int]]) -> int:
      rows, cols = len(grid), len(grid[0])
      def two_dim_to_one_dim(i, j):
        return i * rows + j
      order = []
      for i in range(rows):
        for j in range(cols):
          order.append((grid[i][j], i, j))
      order.sort()
      uf = UF(rows * cols)
      for price, i, j in order:
        for nx, ny in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
          if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] <= price:
            uf.union(two_dim_to_one_dim(nx, ny), two_dim_to_one_dim(i, j))
        if uf.find(0) == uf.find(rows * cols - 1):
          return price