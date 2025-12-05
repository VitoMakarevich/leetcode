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
      return self._find_pair(left_list, right_list, target) or self._find_pair(right_list, left_list, target)

    def _to_list(self, tree):
      if tree == None:
        return []
      left = self._to_list(tree.left)
      right = self._to_list(tree.right)
      return left + [tree.val] + right
    

    def _find_pair(self, values, candidates, total):
      start = 0
      for cand in values:
        target = total - cand
        found = bisect_left(candidates, target)
        if found < len(candidates) and candidates[found] == target:
          return True
        start = found
      return False