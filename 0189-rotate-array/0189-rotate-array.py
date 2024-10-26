import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
        return nums
        