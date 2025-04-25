# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
          closest = min(closest, root.val, key = lambda x: (abs(target - x), x))
          if root.val > target:
            root = root.left
          else:
            root = root.right

        return closest

