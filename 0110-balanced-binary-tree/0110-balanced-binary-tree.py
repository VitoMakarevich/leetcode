# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self._dfs(root)

        return res[1]
        
    def _dfs(self, node):
        if node is None:
            return -1, True
        left_depth, left_balanced = self._dfs(node.left)
        if not left_balanced:
          return -1, left_balanced
        right_depth, right_balanced = self._dfs(node.right)
        if not right_balanced:
          return -1, right_balanced
        
        return 1 + max(left_depth, right_depth), abs(left_depth - right_depth) < 2 and left_balanced and right_balanced
        