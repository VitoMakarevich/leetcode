class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      return self._inner(nums, k) - self._inner(nums, k - 1)

    def _inner(self, nums, k):
      res = 0
      left, right = 0, 0
      storage = defaultdict(int)
      while right < len(nums):
        storage[nums[right]] += 1
        
        while len(storage) > k:
          storage[nums[left]] -= 1
          if storage[nums[left]] == 0:
            del storage[nums[left]]
          left += 1
        res += right - left + 1
        right += 1
      return res

