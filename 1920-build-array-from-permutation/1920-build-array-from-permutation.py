class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for v in nums:
          res.append(nums[v])
        return res