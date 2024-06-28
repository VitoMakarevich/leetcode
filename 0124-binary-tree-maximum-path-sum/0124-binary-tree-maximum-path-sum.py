# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      return max(self._maxPathSum(root))
 
    def _maxPathSum(self, root):
      if root is None:
        return [float('-inf'), float('-inf')]
      left = self._maxPathSum(root.left)
      right = self._maxPathSum(root.right)

      maxIfWithCurrent = max(
        root.val + left[0],
        root.val + right[0],
        root.val
      )
      maxIfEndHere = max(root.val + left[0] + right[0], root.val)

      res = [maxIfWithCurrent, max(maxIfEndHere, left[1], right[1], left[0], right[0])]
      return res