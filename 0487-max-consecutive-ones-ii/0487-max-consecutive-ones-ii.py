class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        left = 0
        zero_count = 0
        ans = 0
        while i < len(nums):
          if nums[i] == 0:
            zero_count += 1
          while zero_count == 2:
            if nums[left] == 0:
              zero_count -= 1
            left += 1
          ans = max(ans, i - left + 1)
          i += 1
        return ans