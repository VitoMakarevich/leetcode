class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
          return [-1, -1]
        right = len(nums) - 1
        left = self.bisect_left(nums, target, 0)

        if nums[left] != target:
          return [-1, -1]
        right = self.bisect_right(nums, target, left)
        return [left, right - 1]



    def bisect_left(self, nums, target, low):
      high = len(nums) - 1
      while low < high:
        
        mid = (low + high) // 2
        print(low, high, mid)
        if nums[mid] >= target:
          high = mid
        else:
          low = mid + 1
      return low

    def bisect_right(self, nums, target, low):
      high = len(nums)
      while low < high:
        mid = (low + high) // 2
        if nums[mid] <= target:
          low = mid + 1
        else:
          high = mid
      return low