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
      def dfs(node, path):
        path.append(node)
        if node.val == p.val:
          return
        elif node.val < p.val:
          dfs(node.right, path)
        else:
          dfs(node.left, path)
        
      path = []
      dfs(root, path)
      path.pop()
      while path and path[-1].val < p.val:
        path.pop()
      return path[-1] if path else None
          
            
            