class Solution:
    def candy(self, ratings: List[int]) -> int:
      ratings_sum = [1] * len(ratings)
      for idx in range(1, len(ratings)):
        if ratings[idx] > ratings[idx - 1]:
          ratings_sum[idx] = ratings_sum[idx - 1] + 1
      res = ratings_sum[-1]
      for idx in range(len(ratings) - 2, -1, -1):
        if ratings[idx] > ratings[idx + 1]:
          ratings_sum[idx] = max(ratings_sum[idx], ratings_sum[idx + 1] + 1)
        res += ratings_sum[idx]
      return res