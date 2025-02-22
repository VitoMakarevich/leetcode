
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) 
        self.rank = [1] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
 
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):

        return self.find(x) == self.find(y)

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        connections.sort(key = lambda x: x[2])
        visited = set()
        total = 0
        for conn in connections:
          l, r, price = conn
          if uf.find(l) != uf.find(r):
            uf.union(l, r)
            total += price
        root = uf.find(1)
        for i in range(2, n + 1):
          if uf.find(i) != root:
            return -1
        return total
        