class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
      l = 0
      r = len(nums) - 1
      while l < r:
        mid = l + (r - l) // 2
        mid = mid - 1 if mid % 2 == 1 else mid
        if nums[mid] == nums[mid + 1]:
          l = mid + 2
        else:
          r = mid
      return nums[l]
