class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        counter = 1
        prev = nums[0]
        for v in nums:
          if v != prev:
            counter += 1
          if counter == 3:
            return v
          prev = v
        return nums[0]