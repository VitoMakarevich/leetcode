# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = [0]
        self._dfs(root, counter, float('-inf'))
        return counter[0]
    def _dfs(self, root, counter, prev):
        if prev <= root.val:
            counter[0] += 1
        new_prev = max(prev, root.val)
        if root.left:
            self._dfs(root.left, counter, new_prev)
        if root.right:
            self._dfs(root.right, counter, new_prev)