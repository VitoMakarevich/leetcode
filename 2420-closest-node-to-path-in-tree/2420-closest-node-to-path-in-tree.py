EMPTY_LIST = []
class TreeNode:
  def __init__(self):
    self.adj = EMPTY_LIST
  def add_adj(self, adj):
    if self.adj is EMPTY_LIST:
      self.adj = [adj]
    else:
      self.adj.append(adj)

  def __repr__(self):
    return f"{self.adj}"

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
      graph = self._build_graph(n, edges)
      self.graph = graph

      res = []
      for p_start, p_end, target_node in query:
        nodes_on_path = set()
        self._find_path(p_start, p_end, nodes_on_path)
        closest = self._find_closest(target_node, nodes_on_path)
        res.append(closest)

      return res

    def _find_closest(self, start, path_nodes):
      q = deque([start])
      visited = set()
      while q:
        for i in range(len(q)):
          cur = q.popleft()
          visited.add(cur)
          if cur in path_nodes:
            return cur
          for adj in self.graph[cur].adj:
            if not adj in visited:
              q.append(adj)
          


    def _find_path(self, root, target, path):
      path.add(root)
      if root == target:
        return True
      for adj in self.graph[root].adj:
        if not adj in path:
          res = self._find_path(adj, target, path)
          if res:
            return res
      path.remove(root)
      return False

    def _build_graph(self, n, edges):
      graph = []
      for i in range(n):
        graph.append(TreeNode())
      for left, right in edges:
        graph[left].add_adj(right)
        graph[right].add_adj(left)

      return graph