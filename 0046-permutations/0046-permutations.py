class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def inner(nums, perm = [], res=[]):
          if not nums:
            res.append(perm[::])
          for i in range(len(nums)):
            new_nums = nums[:i] + nums [i + 1:]
            perm.append(nums[i])
            inner(new_nums, perm, res)
            perm.pop()
          return res

        return inner(nums)