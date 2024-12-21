import time

class GraphNode:
  def __init__(self, color):
    self.color = color
    self.adj = []
  def add_adj(self, adj):
    self.adj.append(adj)
def measure(func):
  def wrapper(*args, **kwargs):
      start_time = time.perf_counter()
      result = func(*args, **kwargs)
      end_time = time.perf_counter()
      print(f"Execution time: {end_time - start_time:.5f} s")
      return result
  return wrapper

class Solution:

    # topological sort
    # detect loops
    # if no loops - DP from each topological sort start for longest path and path color count
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
      
      self.graph = self.build_graph(colors, edges)
      roots = self.topological_sort(self.graph, colors)
      r = self.detect_loops_root(roots)

      if r == -1:
        return -1
      return self.longest_path_root(roots)
    @measure
    def build_graph(self, colors, edges):
      graph = []
      for color in colors:
        graph.append(GraphNode(color))
      for edge in edges:
        graph[edge[0]].add_adj(edge[1])
      return graph

    @measure
    def longest_path_root(self, roots):
      res = (-1, 'a')
      for root in roots:
        root_max = self.longest_path(root)
        for color, count in root_max.items():
          if count > res[0]:
            res = (count, color)
      return res[0]

    @measure
    def topological_sort(self, graph, colors):
      visited = set()
      for node in graph:
        for adj in node.adj:
          visited.add(adj)
      roots = set()
      for i in range(len(colors)):
        if not i in visited:
          roots.add(i)
      return roots

    @measure
    def detect_loops_root(self, roots):
      if len(roots) == 0:
        return -1
      visited = set()
      for root in roots:
        res = self.detect_loops(self.graph[root], root, set(), visited)
        if res:
          return -1
      if len(visited) < len(self.graph):
        return -1
      
    def detect_loops(self, cur, cur_id, path, visited):
      if cur_id in visited:
        return False
      visited.add(cur_id)
      path.add(cur_id)
      for adj in cur.adj:
        if adj in path:
          return True
        loop_in_this = self.detect_loops(self.graph[adj], adj, path, visited)
        if loop_in_this:
          return True
      path.remove(cur_id)
      return False

    @cache
    def longest_path(self, cur):
      node = self.graph[cur]
      candidates = []
      for adj in node.adj:
        candidate = self.longest_path(adj)
        candidates.append(candidate)
      if len(candidates):
        cum_res = {}
        for cand in candidates:
          for color, count in cand.items():
            cum_res[color] = max(count, cum_res.get(color, 0))
        cum_res[node.color] = cum_res.get(node.color, 0) + 1
        return cum_res
      else:
        return {
          node.color: 1
        }

