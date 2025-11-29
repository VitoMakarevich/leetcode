"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
      if not root:
        return None
      cur = deque([root])
      while cur:
        level = []
        for _ in range(len(cur)):
          node = cur.popleft()
          level.append(node)
          if node.left:
            cur.append(node.left)
          if node.right:
            cur.append(node.right)
        level.append(None)
        for prev, nxt in zip(level, level[1:]):
          prev.next = nxt
      return root