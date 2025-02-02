class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
      cache = defaultdict(list)
      cur_path = []
      target = len(graph) - 1
      res = []
      def _dfs(node):
        if node == target:
          return [[node]]
        if not node in cache:
          cur_path.append(node)
          local_r = []
          for adj in graph[node]:
            paths = _dfs(adj)
            if len(paths) > 0:
              for p in paths:
                res.append(cur_path + p)
                local_r.append([node] + p)
          cache[node] = local_r
          cur_path.pop()
        return cache[node]
      return _dfs(0)