class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = 0
        for n in nums:
            mask = 1 << n
            if memo & mask:
                return n
            else:
                memo |= mask
        