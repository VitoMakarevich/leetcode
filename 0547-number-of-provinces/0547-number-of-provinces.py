class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(visited, isConnected, i)
                res += 1
        return res

        
    def dfs(self, visited, isConnected, city):
        visited.add(city)
        for neighbour in self.neighbors(city, isConnected):
            if not neighbour in visited:
                self.dfs(visited, isConnected, neighbour)

    def neighbors(self, i, isConnected):
        res = []
        for index, v in enumerate(isConnected[i]):
            if v == 1:
                res.append(index)
        return res
