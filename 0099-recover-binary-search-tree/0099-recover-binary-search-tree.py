# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
          if not node:
            return []
          return inorder(node.left) + [(node.val, node)] + inorder(node.right)
        ordered = inorder(root)
        ordered = [(idx, v) for idx, v in enumerate(ordered)]
        ordered.sort(key = lambda x: x[1][0])
        to_swap = []
        for correct_idx, v in enumerate(ordered):
          initial_idx, v = v
          value, node = v
          if initial_idx != correct_idx:
            to_swap.append(node)

        temp = to_swap[0].val
        to_swap[0].val = to_swap[1].val
        to_swap[1].val = temp
