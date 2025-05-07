class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for v in range(n)]
        for source, target, price in flights:
            adj[source].append((target, price))
        prev = [inf] * n
        prev[src] = 0
        
        changed = False
        for v in range(k + 1):
            changed = False
            cur = list(prev)
            
            for vertex in range(n):
                for target, price in adj[vertex]:
                    if prev[vertex] + price < cur[target]:
                        cur[target] = prev[vertex] + price
                        changed = True
            if changed == False:
                break
            prev = cur
        return cur[dst] if cur[dst] != inf else -1