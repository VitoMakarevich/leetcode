class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7

        def kadane(nums):
            max_sum = curr = 0
            for x in nums:
                curr = max(x, curr + x)
                max_sum = max(max_sum, curr)
            return max_sum

        max_kadane = kadane(arr)

        if k == 1:
            return max_kadane % mod

        # Compute prefix and suffix max
        total = sum(arr)
        prefix = curr = 0
        max_prefix = 0
        for x in arr:
            curr += x
            max_prefix = max(max_prefix, curr)

        suffix = curr = 0
        max_suffix = 0
        for x in reversed(arr):
            curr += x
            max_suffix = max(max_suffix, curr)

        if total > 0:
            result = max(max_kadane, max_prefix + max_suffix + (k - 2) * total)
        else:
            # Only up to two copies matter
            double_kadane = kadane(arr + arr)
            result = max(max_kadane, double_kadane)

        return result % mod
