# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
      if p.right:
        res = p.right
        cur = p.right
        while cur:
          res = cur
          cur = cur.left
        return res
      def dfs(prev, node, direction):
        if node.val == p.val:
          return prev if direction == 'l' else None
        elif node.val < p.val:
          return dfs(node, node.right, 'r')
        return dfs(node, node.left, 'l')
        
      return dfs(None, root, 'r')
          
            
            