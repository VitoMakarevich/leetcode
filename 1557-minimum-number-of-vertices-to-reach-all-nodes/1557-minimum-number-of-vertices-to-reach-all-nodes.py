class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for e in edges:
          source, target = e
          graph[target] = True
          graph[source] = graph.get(source, False) or False
        
        return [index for index, value in graph.items() if not value ]