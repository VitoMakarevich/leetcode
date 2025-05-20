class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits_by_user = defaultdict(list)
        for user, ts, website in zip(username, timestamp, website):
          visits_by_user[user].append((ts, website))
        pattern_and_score = defaultdict(set)
        for user in visits_by_user.keys():
          visits_by_user[user].sort(key = lambda x: x[0])
          sites = list(map(lambda x: x[1], visits_by_user[user]))
          for idx1, s1 in enumerate(sites):
            for idx2, s2 in enumerate(sites[idx1 + 1:], start = idx1 + 1):
              for s3 in sites[idx2 + 1:]:
                pattern = (s1, s2, s3)

                pattern_and_score[pattern].add(user)
        res = ()
        count = 0
        for pattern, users in pattern_and_score.items():
          score = len(users)
          if score > count or (score == count and pattern < res) or not res:
            count = score
            res = pattern
        return res

        