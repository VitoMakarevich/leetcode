# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
      return max(self._dfs(root))
    
    def _dfs(self, root):
      if not root:
        return (0, 0)
      if_root_val = root.val
      if_left_root, if_left_childs = self._dfs(root.left)
      if_right_root, if_right_childs = self._dfs(root.right)
      res = (if_root_val + if_left_childs + if_right_childs, max(if_left_root, if_left_childs) + max(if_right_root, if_right_childs))
      return res