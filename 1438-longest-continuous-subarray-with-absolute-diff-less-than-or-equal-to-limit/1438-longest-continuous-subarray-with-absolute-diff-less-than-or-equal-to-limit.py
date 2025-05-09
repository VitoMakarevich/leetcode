class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        r = 0
        l = 0
        max_h = []
        min_h = []
        res = 0
        while r < len(nums):
          heapq.heappush(max_h, (-nums[r], r))
          heapq.heappush(min_h, (nums[r], r))

          while -max_h[0][0] - min_h[0][0] > limit:
            l = min(max_h[0][1], min_h[0][1]) + 1

            while min_h[0][1] < l:
              heapq.heappop(min_h)
            while max_h[0][1] < l:
              heapq.heappop(max_h)
          res = max(res, r - l + 1)
          r += 1
        return res