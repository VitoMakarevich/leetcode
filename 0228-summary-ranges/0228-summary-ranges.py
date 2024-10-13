class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        prev = nums[0]
        start = nums[0]
        for v in nums[1:]:
            if v - prev == 1:
                prev = v
            else:
                res.append(self._format_result(start, prev))
                start = v
                prev = v

        res.append(self._format_result(start, prev))

        return res

    def _format_result(self, start, prev):
        if start == prev:
            return f"{prev}"
        else:
            return f"{start}->{prev}"