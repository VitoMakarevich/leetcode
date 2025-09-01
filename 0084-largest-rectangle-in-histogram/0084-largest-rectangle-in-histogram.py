class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
      s = [-1]
      res = 0
      for idx in range(len(bars)):
        while s[-1] != -1 and bars[s[-1]] >= bars[idx]:
          height = bars[s.pop()]
          width = idx - s[-1] - 1
          res = max(res, height * width)
        s.append(idx)
      while s[-1] != -1:
        height = bars[s.pop()]
        width = len(bars) - s[-1] - 1
        res = max(res, height * width)
      return res

