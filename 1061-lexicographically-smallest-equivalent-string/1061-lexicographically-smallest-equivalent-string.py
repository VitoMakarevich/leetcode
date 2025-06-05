class UF:
  def __init__(self, size):
    self._parent = [x for x in range(size)]
    self._count = [1] * size
  
  def find(self, node):
    if self._parent[node] != node:
      self._parent[node] = self.find(self._parent[node])
    return self._parent[node]
  
  def union(self, a, b):
    root_a = self.find(a)
    root_b = self.find(b)

    if self._count[root_a] < self._count[root_b]:
      root_a, root_b = root_b, root_a
    
    self._parent[root_b] = root_a
    self._count[root_a] += self._count[root_b]
    

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
      uf = UF(26)
      for v1, v2 in zip(s1, s2):
        uf.union(ord(v1) - ord('a'), ord(v2) - ord('a'))
      
      smallest_per_parent = [x for x in range(26)]
      for cand in range(26):
        root = uf.find(cand)
        smallest = min(cand, smallest_per_parent[root])
        smallest_per_parent[cand] = smallest
        smallest_per_parent[root] = smallest
      res = ''
      for char in baseStr:
        root = uf.find(ord(char) - ord('a'))
        smallest = smallest_per_parent[root]
        res += chr(ord('a') + smallest)
      return res