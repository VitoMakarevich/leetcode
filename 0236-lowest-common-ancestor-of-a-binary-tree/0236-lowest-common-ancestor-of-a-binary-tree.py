# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      p1 = queue.deque([])
      p2 = queue.deque([])
      self._findPath(root, p, p1)
      self._findPath(root, q, p2)
      lca = p2[0]
      for i in range(0, min(len(p1), len(p2))):
        if p1[i] == p2[i]:
          lca = p1[i]
  
      return lca

    def _findPath(self, root, target, queue):
      queue.append(root)
      # print(list(map(lambda x: x.val if x is not None else None, queue)))
      if root == target:
        return True
      elif root is None:
        queue.pop()
        return False
      else:
        res = self._findPath(root.left, target, queue) or self._findPath(root.right, target, queue)
        if not res:
          queue.pop()
        return res
