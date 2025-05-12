class UnionFind:
  def __init__(self, count):
    self._root = [i for i in range(count)]
    self._counts = [1 for i in range(count)]

  def find(self, x):
    parent = self._root[x]
    if not parent == x:
      self._root[x] = self.find(parent)
    return self._root[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x == root_y:
      return False

    if self._counts[root_x] < self._counts[root_y]:
      root_x, root_y = root_y, root_x
    
    self._root[root_y] = root_x
    self._counts[root_x] += self._counts[root_y]
    return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for source, target in edges:
          n -= uf.union(source, target)
        return n or 1