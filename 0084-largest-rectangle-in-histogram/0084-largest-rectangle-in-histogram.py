class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        q, res = [], 0
        for bar in bars + [-1]:
          width = 0
          while q and q[-1][0] > bar:
            last_size, w = q.pop()
            width += w
            res = max(res, width * last_size)
          q.append((bar, 1 + width))
        return res