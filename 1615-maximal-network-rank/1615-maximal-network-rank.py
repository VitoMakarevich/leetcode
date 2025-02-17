class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for r in roads:
          left, right = r
          graph[left].add(right)
          graph[right].add(left)
        res = 0
        for source in range(0, n):
          for target in range(source + 1, n):
            r = len(graph[source]) + len(graph[target]) - (source in graph[target])
            res = max(r, res)
        return res