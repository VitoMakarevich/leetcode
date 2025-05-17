class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(0, nums, res, [])
        return res
    
    def backtrack(self, idx, nums, res, prev):
     
      res.append(list(prev))
      for next_idx in range(idx, len(nums)):
        if next_idx != idx and nums[next_idx] == nums[next_idx - 1]:
          continue
        prev.append(nums[next_idx])
        self.backtrack(next_idx + 1, nums, res, prev)
        prev.pop()