from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for target, source in prerequisites:
          graph[target].append(source)
        res = []
        visited = set()
        def dfs(idx, visiting):
          if idx in visiting:
            return False
          if idx in visited:
            return True
          
          visiting.add(idx)
          for predecessor in graph[idx]:
            cycle = dfs(predecessor, visiting)
            if not cycle:
              return False
          res.append(idx)
          visiting.remove(idx)
          visited.add(idx)
          return True
        for cource in range(numCourses):
          if cource not in visited: 
            cycle = dfs(cource, set())
            if not cycle:
              return []
        return res if len(res) == numCourses else []
        

    

