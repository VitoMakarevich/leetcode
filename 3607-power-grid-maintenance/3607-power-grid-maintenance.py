class UF:
  def __init__(self, count):
    self.parent = [idx for idx in range(count)]
    self.size = [1] * count

  def find(self, node):
    if self.parent[node] != node:
      self.parent[node] = self.find(self.parent[node])
    return self.parent[node]
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if self.size[root_y] > self.size[root_x]:
      root_x, root_y = root_y, root_x
    
    self.parent[root_y] = root_x
    self.size[root_x] += self.size[root_y]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
      uf = UF(c)
      for source, target in connections:
        uf.union(source - 1, target - 1)
      sets = {}
      for node in range(c):
        parent = uf.find(node)
        if not parent in sets:
          sets[parent] = SortedSet()
        sets[parent].add(node)
      res = []
      for action, node in queries:
        node -= 1
        parent = uf.find(node)
        if action == 1:
          if len(sets[parent]) == 0:
            res.append(-1)
          elif node in sets[parent]:
            res.append(node + 1)
          else:
            res.append(sets[parent][0] + 1)
        else:
          sets[parent].discard(node)
      return res


    
