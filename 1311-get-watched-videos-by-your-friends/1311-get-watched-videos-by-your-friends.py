class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = [set() for _ in range(len(friends))]
        for source in range(len(friends)):
          for target in friends[source]:
            if not source == target:
              graph[source].add((target, 1))
              graph[target].add((source, 1))
        
        friends_at_level = self.find_friends_at_level(level, graph, id)
        
        video_with_watch_count = Counter()
        for friend in friends_at_level: 
          for video in watchedVideos[friend]:
            video_with_watch_count[video] += 1
        
        res = []
        for video_name, count in video_with_watch_count.items():
          res.append((count, video_name))
        res.sort()
        return list(map(lambda x: x[1], res))

    def find_friends_at_level(self, level, graph, start):
      pq = [(0, start)]
      visited = set()
      distances = [inf for i in range(len(graph))]
      distances[start] = 0
      res = set()
      while pq and pq[0][0] <= level:
        price, cur = heappop(pq)
        if cur in visited:
          continue
        visited.add(cur)
        for adj, adj_price in graph[cur]:
          potential_price = price + adj_price
          if potential_price <= distances[adj]:
            if potential_price == level:
              res.add(adj)
            elif potential_price < level:
              res.discard(adj)
            distances[adj] = potential_price
            heappush(pq, (potential_price, adj))
      return res