class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
      intervals = []
      for index in range(len(ranges)):
        cur_range = ranges[index]
        if cur_range != 0:
          intervals.append(
            (
              max(0, index - cur_range), min(index + cur_range, n)
            )
          )
      intervals.sort(key = lambda x: (x[0], -x[1]))
      if len(intervals) == 0:
        return -1
      prev_interval_end = intervals[0][1]
      ans = 1
      idx = 1
      while prev_interval_end < n:
        next_interval_end = prev_interval_end
        while idx < len(intervals) and intervals[idx][0] <= prev_interval_end:
          next_interval_end = max(next_interval_end, intervals[idx][1])
          idx += 1
        if next_interval_end == prev_interval_end:
          return -1
        ans += 1
        prev_interval_end = next_interval_end
      return ans