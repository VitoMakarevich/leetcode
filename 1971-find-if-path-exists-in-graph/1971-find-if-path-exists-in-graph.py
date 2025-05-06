class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for v in range(0, n)]
        for s, target in edges:
            adj[s].append(target)
            adj[target].append(s)
        visited = set()
        return self._dfs(source, adj, visited, destination)

    def _dfs(self, node, adj, visited, target):
        if node == target:
            return True
        visited.add(node)
        for neigh in adj[node]:
            if not neigh in visited:
                res = self._dfs(neigh, adj, visited, target)
                if res:
                    return True
        return False