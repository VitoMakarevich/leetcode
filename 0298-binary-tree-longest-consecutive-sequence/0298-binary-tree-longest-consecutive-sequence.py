# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # incl, not-incl
        def dfs(root, prev, length):
          if not root:
            return length
          length = length + 1 if prev and root.val == prev.val + 1 else 1
          return max(length, max(dfs(root.left, root, length), dfs(root.right, root, length)))
          


        return dfs(root, None, 0)