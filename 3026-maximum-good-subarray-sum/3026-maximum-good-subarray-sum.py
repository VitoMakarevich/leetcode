from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        values = defaultdict(list)
        for idx, val in enumerate(nums):
            values[val].append(idx)
        
        res = -inf

        for val, indices in values.items():
            neighbors = []
            if val + k in values:
                neighbors += values[val + k]
            if val - k in values:
                neighbors += values[val - k]

            for i in indices:
                for j in neighbors:
                    a, b = min(i, j), max(i, j)
                    s = prefix_sum[b + 1] - prefix_sum[a]
                    res = max(res, s)

        return res if res != -inf else 0
