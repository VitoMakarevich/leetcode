class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
      distances_from_first = self.distance_to(edges, node1)
      distances_from_second = self.distance_to(edges, node2)
      res = inf
      res_idx = -1
      for idx in range(len(edges)):
        max_dist = max(distances_from_first[idx], distances_from_second[idx])
        if max_dist < res:
          res = max_dist
          res_idx = idx
      return res_idx

    def distance_to(self, graph, start):
      out = [inf] * len(graph)
      visited = [False] * len(graph)
      out[start] = 0
      def dfs(node, depth):
        if visited[node]:
          return
        visited[node] = True
        out[node] = depth
        next_node = graph[node]
        if next_node != -1 and not visited[next_node]:
          dfs(next_node, depth + 1)
      dfs(start, 0)
      return out
