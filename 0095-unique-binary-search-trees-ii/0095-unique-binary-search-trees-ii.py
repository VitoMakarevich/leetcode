# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self._res = []
        return self._dp(1, n)
        
    @cache
    def _dp(self, start, end):
      if start > end:
        return [None]
      
      trees = []
      for mid in range(start, end + 1):
        left_tree = self._dp(start, mid - 1)
        right_tree = self._dp(mid + 1, end)

        for l in left_tree:
          for r in right_tree:
            head = TreeNode(mid, l, r)
            trees.append(head)
      return trees