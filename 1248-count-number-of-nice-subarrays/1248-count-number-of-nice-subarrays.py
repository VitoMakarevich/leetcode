class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        prev_start = -1
        stack = deque()
        nums = [1] + nums + [1]
        res = 0
        while right < len(nums):
          if nums[right] % 2:
            stack.append(right)
          if len(stack) == k + 2:
            res += (stack[1] - stack[0]) * (stack[-1] - stack[-2])
            stack.popleft()
          right += 1
        return res

          

          