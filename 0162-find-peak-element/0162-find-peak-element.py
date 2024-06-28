import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      start = 0
      end = len(nums) - 1
      res = self.search(nums, 0, len(nums) - 1)
      return res
      
    def search(self, nums, start, end):
        if start > end:
          return None
        mid = math.floor((end - start) / 2) + start
        left_smaller = mid - 1 < 0 or nums[mid - 1] < nums[mid]
        right_smaller = mid + 1 == len(nums) or nums[mid + 1] < nums[mid]
        if left_smaller and right_smaller:
          return mid
        res_left = self.search(nums, start, mid - 1)
        if res_left is not None:
          return res_left
        return self.search(nums, mid + 1, end)

