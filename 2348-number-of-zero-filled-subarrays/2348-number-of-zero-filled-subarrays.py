class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
      output = 0
      left = 0
      nums += [20]
      for right, v in enumerate(nums):
        if v != 0:
          while left <= right and nums[left] != 0:
            left += 1

          if left <= right and nums[left] == 0:
            diff = right - left
            output += ((1 + diff) * diff) // 2
            left = right
      return output