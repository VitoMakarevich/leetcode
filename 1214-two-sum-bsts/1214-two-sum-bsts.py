# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
      left_list = self._to_list(root1)
      right_list = self._to_list(root2)
      left = 0
      right = len(right_list) - 1
      while left < len(left_list) and right >= 0:
        if left_list[left] + right_list[right] == target:
          return True
        elif left_list[left] + right_list[right] < target:
          left += 1
        else:
          right -= 1
      return False

    def _to_list(self, tree):
      if tree == None:
        return []
      left = self._to_list(tree.left)
      right = self._to_list(tree.right)
      return left + [tree.val] + right