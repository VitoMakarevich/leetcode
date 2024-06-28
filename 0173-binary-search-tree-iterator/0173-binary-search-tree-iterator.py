# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    res = []
    cur_idx = 0

    def __init__(self, root: Optional[TreeNode]):
      self.res = []
      self.cur_idx = 0
      self._dig(root)

    def _dig(self, node):
      if node.left:
        self._dig(node.left)
      self.res.append(node.val)
      if node.right:
        self._dig(node.right)

    def next(self) -> int:
      res = self.res[self.cur_idx]
      self.cur_idx += 1
      return res

    def hasNext(self) -> bool:
      return self.cur_idx < len(self.res)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()