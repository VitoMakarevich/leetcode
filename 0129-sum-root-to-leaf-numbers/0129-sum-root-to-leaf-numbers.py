# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        values = []
        stack = []
        if root is not None:
          self.sum_inner(root, stack, values)

        return int(reduce(lambda x, y: x + y, values))

    def sum_inner(self, node, stack, values):
      stack.append(node.val)
      if node.left is not None:
        self.sum_inner(node.left, stack, values)
      if node.right is not None:
        self.sum_inner(node.right, stack, values)
      if node.left is None and node.right is None:
        current_path_value = 0
        stack_len = len(stack) - 1
        for index, val in enumerate(stack):
          current_path_value += val * math.pow(10, stack_len - index)
        values.append(current_path_value)
      
      stack.pop()
    
