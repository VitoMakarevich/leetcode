class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        left = 0
        res = 0
        hm = defaultdict(int)
        maxCnt = 0
        for right in range(n):
            hm[nums[right]] += 1
            maxCnt = max(maxCnt, hm[nums[right]])
            if maxCnt + k < right-left+1:
                hm[nums[left]] -= 1
                left += 1
            if maxCnt + k >= right-left+1:
                res = max(res, maxCnt)
        return res