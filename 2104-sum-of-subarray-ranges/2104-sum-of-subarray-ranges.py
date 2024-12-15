class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        l = len(nums)
        r = 0
        for i in range(l):
          min_value = nums[i]
          max_value = nums[i]
          for j in range(i + 1, l):
            min_value = min(min_value, nums[j])
            max_value = max(max_value, nums[j])

            r += max_value - min_value

        return r
        