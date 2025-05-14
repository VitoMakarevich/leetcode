class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

      friends_at_level = self.find_friends_at_level(level, friends, id)
      
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
      queue = deque([start])
      visited = set([start])
      while queue and level > 0:
        
        for _ in range(len(queue)):
          cur = queue.popleft()
          for adj in graph[cur]:
            if not adj in visited:
              visited.add(adj)
              queue.append(adj)
        level -= 1
      return queue
