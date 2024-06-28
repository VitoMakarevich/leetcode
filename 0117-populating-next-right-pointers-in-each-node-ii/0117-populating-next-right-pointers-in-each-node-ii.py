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
    def connect(self, root: 'Node') -> 'Node':
        levels = {}
        
        self.dig(root, levels, 0)
        for level in levels.values():
          for value1, value2 in zip(level, level[1:]):
            value1.next = value2
        return root

    def dig(self, node, levels, level):
        if node is None:
          return
        if not level in levels:
          levels[level] = []

        levels[level].append(node)
        self.dig(node.left, levels, level + 1)
        self.dig(node.right, levels, level + 1)        


        
        

        
