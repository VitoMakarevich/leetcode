"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
      return self._construct(grid, 0, 0, len(grid) - 1, len(grid) - 1)

    def _mid_floor(self, i, j):
      return i + math.floor((j - i) / 2)
    
    def _mid_ceil(self, i, j):
      return i + math.ceil((j - i) / 2)
    
    def _construct(self, grid, top_left_x, top_left_y, bot_right_x, bot_right_y):
      print(top_left_x, top_left_y, bot_right_x, bot_right_y)
      v = grid[top_left_y][top_left_x]
      for x in range(top_left_x, bot_right_x + 1):
        for y in range(top_left_y, bot_right_y + 1):
          if v != grid[y][x]:
            x = float('inf')
            y = float('inf')
            print(f"running with top_left([{top_left_x}, {top_left_y}]), bot_right([{self._mid_ceil(top_left_x, bot_right_x)}, {self._mid_ceil(top_left_y, bot_right_y)}])")
            top_left = self._construct(
              grid,
              top_left_x,
              top_left_y,
              self._mid_floor(top_left_x, bot_right_x),
              self._mid_floor(top_left_y, bot_right_y)
            )
            top_right = self._construct(
              grid,
              self._mid_ceil(top_left_x, bot_right_x),
              top_left_y,
              bot_right_x,
              self._mid_floor(top_left_y, bot_right_y)
            )
            bot_left = self._construct(
              grid,
              top_left_x,
              self._mid_ceil(top_left_y, bot_right_y),
              self._mid_floor(top_left_x, bot_right_x),
              bot_right_y
            )
            bot_right = self._construct(
              grid,
              self._mid_ceil(top_left_x, bot_right_x),
              self._mid_ceil(top_left_y, bot_right_y),
              bot_right_x,
              bot_right_y
            )
            return Node(0, False, top_left, top_right, bot_left, bot_right)
      return Node(v, True, None, None, None, None)
            
