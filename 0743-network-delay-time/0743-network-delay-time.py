class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for i in range(n + 1)] 
        distances = [inf for i in range(n + 1)]
        for source, target, price in times:
          adj[source].append((target, price))
        distances[k] = 0

        queue = [(0, k)]
        while queue:
          distance, cur = heapq.heappop(queue)
          
          for neighbor, price in adj[cur]:
            if price + distance < distances[neighbor]:
              distances[neighbor] = price + distance

              heapq.heappush(queue, (price + distance, neighbor))
        
        res = max(distances[1:])
        return -1  if res == inf  else res
        
        