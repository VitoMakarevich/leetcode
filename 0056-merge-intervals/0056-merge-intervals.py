class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_int = sorted(intervals, key = lambda x: x[0])
        res.append(sorted_int[0])
        last_used_int = 0

        for item in sorted_int[1:]:
          last_used = res[last_used_int]
          if self.is_intersect(item, last_used):
            res[last_used_int] = self._merge(item, last_used)
          else:
            last_used_int += 1
            res.append(item)
        
        return res

    def is_intersect(self, interval1, interval2): 
      return (interval1[0] >= interval2[0] and interval1[0] <= interval2[1]) or (interval1[1] >= interval2[0] and interval1[1] <= interval2[1])

    def _merge(self, i1, i2):
      return [min(i1[0], i2[0]), max(i1[1], i2[1])]
