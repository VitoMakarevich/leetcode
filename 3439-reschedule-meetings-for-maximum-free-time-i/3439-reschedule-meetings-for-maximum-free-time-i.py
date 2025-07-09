class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
      
      events = [(0, 0)]
      for start, end in zip(startTime, endTime):
        events.append((start, end))
      events.append((eventTime, eventTime))

      pauses = []
      for (s1, e1), (s2, e2) in pairwise(events):
        pauses.append(s2 - e1)
      res = 0
      local_res = 0
      left = 0
      for right in range(len(pauses)):
        local_res += pauses[right]
        if right - left > k:
          local_res -= pauses[left]
          left += 1
        res = max(res, local_res) 

      return res