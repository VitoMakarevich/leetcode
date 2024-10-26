# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        stack = deque()
        res = [0]
        if root:
            self._dfs(root, stack, res, targetSum)
        return res[0]

    def _dfs(self, node, stack, res, target):
        copy = stack.copy()
        while len(copy) > 0:
            sum_with_part = sum(copy) + node.val
            if sum_with_part == target:
                res[0] += 1
            copy.popleft()
        if node.val == target:
            res[0] += 1
        stack.append(node.val)
        if node.left:
            self._dfs(node.left, stack, res, target)
        if node.right:
            self._dfs(node.right, stack, res, target)
        stack.pop()

