# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = None
        def dfs(node, new_left, new_right):
          nonlocal new_root
          if not node:
            return None
          dfs(node.left, node.right, node)
          if not new_root:
            new_root = node
          
          node.left = new_left
          dfs(node.right, None, None)
          node.right = new_right
          
          return node
        dfs(root, None, None)
        return new_root