"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        head, prev = None, None

        def dfs(node):
            nonlocal head, prev
            if not node:
                return

            dfs(node.left)

            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node
            prev = node

            dfs(node.right)

        dfs(root)
        # Make it circular
        head.left = prev
        prev.right = head

        return head
            