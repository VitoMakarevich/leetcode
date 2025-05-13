class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
      graph = [[] for _ in range(n)]
      for idx, (source, target) in enumerate(connections):
        graph[source].append((target, idx))
        graph[target].append((source, idx))
      cycle_nodes = set()
      self.find_cycle_nodes(0, cycle_nodes, n, graph)
      res = []
      for idx in range(len(connections)):
        if not idx in cycle_nodes:
          res.append(connections[idx])
      return res
    def find_cycle_nodes(self, start, cycle_nodes, total_nodes, graph):
      ranks = [None] * total_nodes

      def dfs(node, cur_rank):
        ranks[node] = cur_rank
        min_rank = cur_rank
        for neighbor, connection_idx in graph[node]:
          neighbor_rank = ranks[neighbor]
          if neighbor_rank is None:
            neigh_min_rank = dfs(neighbor, cur_rank + 1)
            if neigh_min_rank <= cur_rank:
              cycle_nodes.add(connection_idx)
            min_rank = min(min_rank, neigh_min_rank)
          elif neighbor_rank != cur_rank - 1:
            min_rank = min(min_rank, neighbor_rank)
            cycle_nodes.add(connection_idx)
        return min_rank
      dfs(0, 0)