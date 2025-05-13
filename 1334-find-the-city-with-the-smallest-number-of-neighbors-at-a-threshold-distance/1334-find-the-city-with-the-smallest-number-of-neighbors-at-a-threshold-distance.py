class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
      adj = [[] for _ in range(n)]
      for source, target, weight in edges:
        adj[source].append((target, weight))
        adj[target].append((source, weight))
      res = (inf, inf)
      for city_idx in range(n):
        neighbors_reacheable = self.neighbors_within_range(city_idx, distanceThreshold, adj, n)
        res = min(res, (neighbors_reacheable, -city_idx))

      return -res[1]

    def neighbors_within_range(self, city, dist, adj, city_count):
      pq = [(0, city)]
      prices = [inf] * city_count
      prices[city] = 0
      visited = set()
      while pq and pq[0][0] <= dist:
        price, cur_city = heappop(pq)
        if cur_city in visited:
          continue
        visited.add(cur_city)
        for neighbor, neighbor_price in adj[cur_city]:
          potential_price = price + neighbor_price
          if potential_price < prices[neighbor]:
            prices[neighbor] = potential_price
            heappush(pq, (potential_price, neighbor))

      return len(visited) - 1