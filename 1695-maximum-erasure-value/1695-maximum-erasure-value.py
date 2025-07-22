class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        store = {}
        counter = 0
        for right in range(len(nums)):
          counter += nums[right]
          if nums[right] in store:
            start = left
            left = store[nums[right]] + 1
            for idx in range(start, store[nums[right]] + 1):
              counter -= nums[idx]
              del store[nums[idx]]
            
          store[nums[right]] = right
          res = max(res, counter)
        return res