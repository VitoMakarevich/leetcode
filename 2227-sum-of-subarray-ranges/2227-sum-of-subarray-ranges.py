class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        l = len(nums)
        min_s = max_s = 0
        s = deque()
        for cur in range(l + 1):
          while s and (cur == l or nums[s[-1]] > nums[cur]):
            last =  s.pop()
            pre_last = s[-1] if s else -1
            min_s += nums[last] * (cur - last) * (last - pre_last)
          s.append(cur)
        s = deque()
        for cur in range(l + 1):
          while s and (cur == l or nums[s[-1]] < nums[cur]):
            last =  s.pop()
            pre_last = s[-1] if s else -1
            max_s += nums[last] * (cur - last) * (last - pre_last)
          s.append(cur)

        return max_s - min_s