class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
      cum_incr = [0] * (length + 1)
      for start, end, val in updates:
        cum_incr[start] += val
        cum_incr[end + 1] -= val
      res = []
      counter = 0
      for i in range(length):
        counter += cum_incr[i]
        res.append(counter)
      return res
