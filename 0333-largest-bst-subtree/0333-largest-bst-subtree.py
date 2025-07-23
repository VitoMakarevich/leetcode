# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
      res = 0
      # if left is valid and right is valid and left < node and right > node:
      # compare res = max(res, 1 + size(left) + size(right)) and return True + number of nodes
      def dfs(node):
        if not node:
          return inf, -inf, 0
        nonlocal res
        left_min, left_max, left_size = dfs(node.left)
        right_min, right_max, right_size = dfs(node.right)
        if left_max < node.val < right_min:
          subtree_size = 1 + left_size + right_size
          res = max(res, subtree_size)
          return min(left_min, node.val), max(right_max, node.val), subtree_size
        else:
          return -inf, inf, 0
          
      dfs(root)
      return res