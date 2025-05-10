# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
      inorder_indexes = {}
      for index, value in enumerate(inorder):
        inorder_indexes[value] = index
      
      def _build(left, right):
        if left > right:
          return None
        head_val = postorder.pop()
        node = TreeNode(head_val)
        
        head_pos = inorder_indexes[head_val]
        node.right = _build(head_pos + 1, right)
        node.left = _build(left, head_pos - 1)
        return node
      return _build(0, len(inorder) - 1)