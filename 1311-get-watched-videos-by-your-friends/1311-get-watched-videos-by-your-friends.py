class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = [set() for _ in range(len(friends))]
        for source in range(len(friends)):
          for target in friends[source]:
            if not source == target:
              graph[source].add((target, 1))
              graph[target].add((source, 1))
        
        friends_at_level = self.find_friends_at_level(level, graph, id)
        
        video_with_watch_count = Counter(
            video
            for friend in friends_at_level
            for video in watchedVideos[friend]
        )

        return [video for video, _ in sorted(video_with_watch_count.items(), key=lambda x: (x[1], x[0]))]
    def find_friends_at_level(self, level, graph, start):
      pq = [(0, start)]
      visited = set()
      distances = [inf for i in range(len(graph))]
      distances[start] = 0
      while pq and pq[0][0] <= level:
        price, cur = heappop(pq)
        if cur in visited:
          continue
        visited.add(cur)
        for adj, adj_price in graph[cur]:
          potential_price = price + adj_price
          if potential_price <= distances[adj]:
            distances[adj] = potential_price
            heappush(pq, (potential_price, adj))
      res = [idx for idx, node in enumerate(distances) if node == level]
      return res