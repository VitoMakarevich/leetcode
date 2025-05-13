import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
       
        def traverse(node):
          if not node:
            return []
          return traverse(node.left) + [node.val] + traverse(node.right)
          
        inorder = traverse(root)
        return inorder[k - 1]
      