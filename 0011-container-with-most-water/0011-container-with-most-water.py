class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = float("-inf")
        left = 0
        right = len(height) - 1
        while left < right:
          cur_height = min(height[left], height[right]) * (right - left)
          mx = max(mx, cur_height)
          if height[left] > height[right]:
            right -= 1
          else:
            left += 1
        return mx