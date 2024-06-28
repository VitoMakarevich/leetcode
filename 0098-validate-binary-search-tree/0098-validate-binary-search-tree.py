# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      return self._isValid(root, float("-inf"), float("inf"))

    def _isValid(self, root, smallest, biggest):
        if root is None:
          return True
        # print(f"checking {root.val} with bounds [{smallest}, {biggest}]")
        node_valid = root.val > smallest and root.val < biggest
        if not node_valid:
          return False
        return node_valid and self._isValid(root.left, smallest, root.val) and self._isValid(root.right, root.val, biggest)
