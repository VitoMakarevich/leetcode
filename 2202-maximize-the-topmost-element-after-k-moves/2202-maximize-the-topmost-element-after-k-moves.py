class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
      size = len(nums)
      if k == 0:
        return nums[0]
      if size == 1:
        if k % 2 == 0:
          return nums[0]
        return -1
      if k >= size:
        return max(nums)
      max_after_k = max(nums[:k - 1], default = 0)
      if_skip_k = nums[k]
      return max(max_after_k, if_skip_k)
