class Twitter:
    MAX_TWEETS = 10
    def __init__(self):
        self._followers = defaultdict(set)
        self._tweets = {}
        self._tweet_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self._tweets:
          self._tweets[userId] = deque()
        if len(self._tweets[userId]) == Twitter.MAX_TWEETS:
          self._tweets[userId].popleft()
        self._tweets[userId].append((self._tweet_counter, tweetId))
        self._tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        idx = -1
        changed = False
        while True:
          changed = False
          for friend_id in list(self._followers[userId]) + [userId]:
            if not friend_id in self._tweets:
              continue
            news = self._tweets[friend_id]
            if abs(idx) > len(news):
              continue
            latest = news[idx]
            if len(q) < Twitter.MAX_TWEETS:
              heapq.heappush(q, latest)
              changed = True
            elif q[0][0] < latest[0]:
              heapq.heappop(q)
              heapq.heappush(q, latest)
              changed = True
          if not changed:
            break
          idx -= 1
        res = []
        while q:
          res.append(heapq.heappop(q)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
      self._followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
      self._followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)