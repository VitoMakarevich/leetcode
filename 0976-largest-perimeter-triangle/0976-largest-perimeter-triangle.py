class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
      nums.sort()
      for bigger_side_idx in range(len(nums) - 1, 1, -1):
        if nums[bigger_side_idx - 2] + nums[bigger_side_idx - 1] > nums[bigger_side_idx]:
          return nums[bigger_side_idx - 2] + nums[bigger_side_idx - 1] + nums[bigger_side_idx]
          
      return 0