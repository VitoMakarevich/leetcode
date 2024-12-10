"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_iter = p
        q_iter = q
        p_path = set()
        while p_iter != None:
          p_path.add(p_iter)
          p_iter = p_iter.parent
        while q_iter not in p_path:
          q_iter = q_iter.parent
        return q_iter