class Solution:
    # without t
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        state = [SortedDict() for _ in range(n)]
        adj = defaultdict(list)
        for source, target, weight in edges:
          adj[source].append((target, weight))
        
        @cache
        def dp(node: int, steps: int, curr_weight: int) -> int:
            if curr_weight >= t:
                return -1
            if steps == 0:
                return curr_weight
            max_path = -1
            for neighbor, weight in adj[node]:
                new_weight = curr_weight + weight
                if new_weight < t:
                    result = dp(neighbor, steps - 1, new_weight)
                    max_path = max(max_path, result)
            return max_path

        res = -1
        for start_node in range(n):
            res = max(res, dp(start_node, k, 0))
        return res