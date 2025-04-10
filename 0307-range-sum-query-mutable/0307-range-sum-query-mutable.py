class NumArray:

    def __init__(self, nums: List[int]):
        self._bits = [0 for _ in range(len(nums) + 1)]
        self._nums = nums
        for idx, value in enumerate(nums):
	        self._update(idx + 1, value)
          

    def update(self, index: int, val: int) -> None:
      diff = val - self._nums[index]
      self._nums[index] = val
      self._update(index + 1, diff)
    
    def _update(self, index: int, diff: int) -> None:
       r = index
       while r <= len(self._nums):
         self._bits[r] += diff
         r += r & (-r)


    def sumRange(self, start: int, end: int) -> int:
      right = self._sum_from_start(end + 1)
      left = self._sum_from_start(start)    
      return right - left

    def _sum_from_start(self, idx: int) -> int:
      res = 0
      while idx > 0:
        res += self._bits[idx]
        idx -= idx & (-idx)
      return res
