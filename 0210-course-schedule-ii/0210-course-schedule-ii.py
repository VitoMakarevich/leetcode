from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_source_to_target = [set() for _ in range(numCourses)]
        graph_target_to_source = [set() for _ in range(numCourses)]   

        for req in prerequisites:
          target = req[0]
          source = req[1]
          graph_source_to_target[source].add(target)
          graph_target_to_source[target].add(source)

        visited = set()   
        chain = deque([])
        iteration = deque([])
        for index, childs in enumerate(graph_target_to_source):
          if len(graph_target_to_source[index]) == 0:
            iteration.append(index)
        
        while iteration:
          nxt = iteration.popleft()
          if nxt in visited:
            continue
          visited.add(nxt)
          chain.append(nxt)
          for child in graph_source_to_target[nxt]:
            graph_target_to_source[child].remove(nxt)
            if len(graph_target_to_source[child]) == 0:
              iteration.append(child)
            
        if len(visited) == numCourses:
          return list(chain)
        else:
          return []
        

    

