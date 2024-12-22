# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
      t, f = self._dp(root)
      return t if result else f

    def _dp(self, root):
      if root.val == 0:
          return 1, 0
      if root.val == 1:
          return 0, 1

      if root.val == 5: # NOT
          t, f = self._dp(root.left or root.right)
          return f, t

      lt, lf = self._dp(root.left)
      rt, rf = self._dp(root.right)
      
      if root.val == 2: # OR
          return min(lt + rt, lf + rt, lt + rf), lf + rf

      if root.val == 3: # AND
          return lt + rt, min(lt + rf, lf + rt, lf + rf)
      
      if root.val == 4: # XOR
          return min(lf + rt, lt + rf), min(lt + rt, lf + rf)