class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        cache = {}
        safe_or_terminal = []
        for index, adj in enumerate(graph):
          if not index in visited:
            is_safe = self._dfs(index, graph, set(), cache)
            if is_safe:
              safe_or_terminal.append(index)
        return safe_or_terminal
    def _dfs(self, node, graph, path, cache):
      if not node in cache:
        is_safe = True
        path.add(node)
        for adj in graph[node]:
          if adj in path:
            res = is_safe = False
            break
          else:
            res = self._dfs(adj, graph, path, cache)
            if not res:
              is_safe = False
              break
        cache[node] = is_safe
        path.remove(node)
      return cache[node]