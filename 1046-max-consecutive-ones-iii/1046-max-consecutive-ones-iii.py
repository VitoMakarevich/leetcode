class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        k_zeroes = 0
        left = 0
        right = 0
        res = float('-inf')
        while right < len(nums):
            if k_zeroes < k and nums[right] == 0:
                k_zeroes += 1
            elif nums[right] == 0:
                while nums[left] != 0:
                    left += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1

        res = max(res, right - left)
        
        return res
                
