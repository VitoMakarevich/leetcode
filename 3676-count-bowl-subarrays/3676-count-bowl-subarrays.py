class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
      return self._inner(nums)

    def _inner(self, nums):
      stack = []
      res = 0
      for idx, val in enumerate(nums):
        added_once = False
        while len(stack) and val > stack[-1]:
          last_item = stack.pop()
          if len(stack):
            res += 1
            added_once = True
        stack.append(val)

      return res