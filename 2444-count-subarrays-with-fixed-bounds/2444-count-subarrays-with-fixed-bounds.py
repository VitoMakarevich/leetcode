class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i = 0
        lists = []
        last_start = -1
        min_v = -1
        max_v = -1
        res = 0
        for i, v in enumerate(nums):
          if v == minK:
            min_v = i
          if v == maxK:
            max_v = i
          if v < minK or v > maxK:
            last_start = i
            min_v = -1
            max_v = -1
          if min_v != -1 and max_v != -1:
            res += min(max_v, min_v) - last_start
        return res
        