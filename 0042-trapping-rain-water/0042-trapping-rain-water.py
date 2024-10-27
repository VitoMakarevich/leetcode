from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        left_border = float('-inf')
        left_border_sizes = [0 for i in range(len(height))]
        left_border_sizes[0] = left_border
        for i, v in enumerate(height[1:], start = 1):
            left_border = max(left_border, height[i - 1])
            left_border_sizes[i] = left_border
        right_border = float('-inf')
        right_border_sizes = [0 for i in range(len(height))]
        right_border_sizes[len(height) - 1] = right_border
        for i, v in reversed(list(enumerate(height[:len(height) - 1]))):
            right_border = max(right_border, height[i + 1])
            right_border_sizes[i] = right_border
        
        # print(left_border_sizes, right_border_sizes)
        res = 0
        for i, v in enumerate(height):
            wall_size = min(right_border_sizes[i], left_border_sizes[i])
            if wall_size > 0:
                res += max(wall_size - v, 0)

        return res 