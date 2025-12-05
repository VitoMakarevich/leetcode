# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
      left_search = self._find(root1, root2, target)
      right_search = self._find(root2, root1, target)
      return left_search or right_search

    def _find(self, left, right, total):
      if left == None:
        return False
      if self._find(left.left, right, total):
        return True
      target = total - left.val
      if self.exists_in(right, target):
        return True
      if self._find(left.right, right, total):
        return True
      return False
    
    def exists_in(self, tree, value):
      if tree == None:
        return False
      if tree.val == value:
        return True
      if value > tree.val:
        return self.exists_in(tree.right, value)
      return self.exists_in(tree.left, value)
      