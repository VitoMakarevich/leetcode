class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        k_zeroes = 0
        left = 0
        right = 0
        res = float('-inf')
        while right < len(nums):
            # print(f"{left}, {right}")
            cur = nums[right]
            if k_zeroes < k:
                if cur == 0:
                    k_zeroes += 1
                    # print(f"adding zero at pos {right}")
            else:
                is_right_zero = nums[right] == 0
                if is_right_zero:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                    # print(f"for right {right} left cut to {left}")
                # print(f"after cut left {left}, right {right}")
            res = max(res, right - left + 1)
            right += 1

        res = max(res, right - left)
        
        return res
                
