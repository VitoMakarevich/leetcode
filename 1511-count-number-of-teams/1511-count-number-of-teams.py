class Solution:
    def numTeams(self, rating: List[int]) -> int:
        self._rating = rating
        res = 0
        length = len(rating)
        for i in range(length - 2):
          res += self._dp_bigger(i, 2)
          res += self._dp_lower(i, 2)
        return res
    @cache
    def _dp_bigger(self, index, remain):
      if index + remain == len(self._rating):
        return 0
      if remain == 0:
        return 1
      res = 0
      for next_index in range(index + 1, len(self._rating)):
        if self._rating[index] < self._rating[next_index]:
          res += self._dp_bigger(next_index, remain -  1)
      return res
     
    @cache
    def _dp_lower(self, index, remain):
      if index + remain == len(self._rating):
        return 0
      if remain == 0:
        return 1
      res = 0
      for next_index in range(index + 1, len(self._rating)):
        if self._rating[index] > self._rating[next_index]:
          res += self._dp_lower(next_index, remain -  1)
      return res
