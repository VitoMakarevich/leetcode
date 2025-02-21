class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visited = set()
        graph = defaultdict(set)
        for index, e in enumerate(edges):
          a, b = e
          graph[a].add((b, succProb[index]))
          graph[b].add((a, succProb[index]))
        probs = defaultdict(int)
        probs[start_node] = 1
        q = [(-1, start_node)]
        while q:

          cur_probability, cur = heapq.heappop(q)
          if cur == end_node:
            return -cur_probability
          if cur in visited:
            continue
          visited.add(cur)
          neighbors = graph[cur]
          for adj, weight in neighbors:
            prob = -cur_probability * weight
            if prob > probs[adj]:
              probs[adj] = prob
              heapq.heappush(q, (-prob, adj))
        return probs[end_node]

