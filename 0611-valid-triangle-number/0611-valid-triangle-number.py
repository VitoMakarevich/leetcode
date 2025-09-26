class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
      nums.sort()
      res = 0
      for biggest in range(len(nums) - 1, 1, -1):
        biggest_size = nums[biggest]
        left, right = 0, biggest - 1
        while left < right:
          if nums[left] + nums[right] > biggest_size:
            res += right - left
            right -= 1
          else:
            left += 1
      return res