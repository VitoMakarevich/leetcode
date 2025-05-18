class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        curr = 0
        left = 0
        for right in range(len(nums)):
          target = nums[right]
          curr += nums[right]
          while (right - left + 1) * target - curr > k:
            curr -= nums[left]
            left += 1
          
          ans = max(ans, right - left + 1)
        return ans
