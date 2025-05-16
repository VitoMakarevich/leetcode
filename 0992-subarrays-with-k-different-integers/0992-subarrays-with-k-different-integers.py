class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      return self._inner(nums, k) - self._inner(nums, k - 1)

    def _inner(self, nums, k):
      res = 0
      left, right = 0, 0
      storage = {}
      while right < len(nums):
        storage[nums[right]] = storage.get(nums[right], 0) + 1
        
        while len(storage) > k:
          left_num = nums[left]
          storage[left_num] -= 1
          if storage[left_num] == 0:
            del storage[left_num]
          left += 1
        res += right - left + 1
        right += 1
      return res

