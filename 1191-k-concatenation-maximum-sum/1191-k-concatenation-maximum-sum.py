class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        def kadane(nums):
            max_ending_here = max_so_far = 0
            for x in nums:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        total_sum = sum(arr)
        max_kadane = kadane(arr)
        if k == 1:
            return max_kadane % mod

        max_kadane_twice = kadane(arr * 2)
        
        prefix_sum = curr = 0
        max_prefix = 0
        for x in arr:
            curr += x
            max_prefix = max(max_prefix, curr)

        suffix_sum = curr = 0
        max_suffix = 0
        for x in reversed(arr):
            curr += x
            max_suffix = max(max_suffix, curr)

        if total_sum > 0:
            result = max(max_kadane_twice, max_prefix + max_suffix + (k - 2) * total_sum)
        else:
            result = max(max_kadane_twice, max_kadane)

        return result % mod
