# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from enum import Enum
from collections import deque

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      d = deque([])
      res = []
      current_order = Direction.LEFT
      if root:
        d.append(root)
      next_elements = deque([])
      while d or next_elements:
        local_res = []
        while d:
          next_item = d.popleft()
          local_res.append(next_item.val)
          if next_item.left:
            next_elements.append(next_item.left)
          if next_item.right:
            next_elements.append(next_item.right)
        
        if current_order == Direction.RIGHT:
          local_res.reverse()
        res.append(local_res)
        while next_elements:
          d.append(next_elements.popleft())
        current_order = Direction.RIGHT if current_order == Direction.LEFT else Direction.LEFT

      return res



