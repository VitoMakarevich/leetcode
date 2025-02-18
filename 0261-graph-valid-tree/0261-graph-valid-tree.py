class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for e in edges:
          e1, e2 = e
          graph[e1].add(e2)
          graph[e2].add(e1)
        prev_level = set()
        prev_level.add(0)
        q = deque()
        for i in graph[0]:
          q.append(i)
        visited = set()
        visited.add(0)
        while q:
          next_level = set()
          cur_level = set()
          for i in range(len(q)):
            item = q.popleft()
            visited.add(item)
            cur_level.add(item)
            neighbors = graph[item]
            if len(neighbors & cur_level) > 0:
              return False
            next_level_neighbors = neighbors - prev_level
            if len(next_level_neighbors & next_level) > 0:
              return False
            next_level |= next_level_neighbors
          prev_level = cur_level
          for i in next_level:
            q.append(i)

          
        return len(visited) == n