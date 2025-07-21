# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
      if root and key == root.val:
        return self._dfs(root, key)
      self._dfs(root, key)
      return root
    def _dfs(self, root, key):
      if not root:
        return None
      if root.val == key:
        if not root.left and not root.right:
          return None
        elif root.right:
          successor = root.right
          while successor and successor.left:
            successor = successor.left
          root.val = successor.val
          root.right = self._dfs(root.right, successor.val)
        else:
          successor = root.left
          while successor and successor.right:
            successor = successor.right
          root.val = successor.val
          root.left = self._dfs(root.left, successor.val)
        return root
      elif root.val > key:
        root.left = self._dfs(root.left, key)
      else:
        root.right = self._dfs(root.right, key)
      return root