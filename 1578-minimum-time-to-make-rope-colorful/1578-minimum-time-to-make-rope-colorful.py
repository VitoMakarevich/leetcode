class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
      prev_color = colors[0]
      max_time = neededTime[0]
      sum_time = max_time
      res = 0
      colors += '0'
      neededTime += [0]
      for color, time in zip(colors[1:], neededTime[1:]):
        if color != prev_color:
          if sum_time > max_time:
            res += sum_time - max_time
          prev_color = color
          max_time = time
          sum_time = time
        else:
          max_time = max(max_time, time)
          sum_time += time
      return res