class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
      first_color, counts = self.neighbors(edges1)
      second_color, second_counts = self.neighbors(edges2)
      biggest_second = 0
      res = []
      for idx, value in enumerate(first_color):
        res.append(counts[first_color[idx]] + max(second_counts))
      return res
      
    def neighbors(self, edges):
      graph = [[] for _ in range(len(edges) * 2)]
      max_node = 0
      for source, target in edges:
        graph[source].append(target)
        graph[target].append(source)
        max_node = max(source, target, max_node)
      if len(graph) - max_node - 1 > 0:
        del graph[-(len(graph) - max_node - 1):]
      color, even_count, odd_count = self.bfs_count(0, graph)

      return color, [even_count, odd_count]
    
    def bfs_count(self, start, graph):
      q = deque([start])
      visited = [False] * len(graph)
      visited[start] = True
      even_res = 0
      odd_res = 0
      distance = 0
      colors = [0] * len(graph)
      while q:
        for _ in range(len(q)):
          cur = q.popleft()
          if distance % 2 == 0:
            even_res += 1
            colors[cur] = 0
          else:
            odd_res += 1
            colors[cur] = 1
          for adj in graph[cur]:
            if not visited[adj]:
              visited[adj] = True
              q.append(adj)
        distance += 1
      return colors, even_res, odd_res

      