class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if lower < nums[0]:
          res.append([lower, nums[0] - 1])
        prev = nums[0]
        for num in nums[1:]:
          if num > prev + 1:
            res.append([prev + 1, num - 1])
          prev = num
        if upper > nums[-1]:
          res.append([nums[-1] + 1, upper])
        return res