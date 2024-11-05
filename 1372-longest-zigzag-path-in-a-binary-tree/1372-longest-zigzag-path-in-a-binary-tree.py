# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = [0]
        if root.left:
            self._dfs(root.left, res, True)
        if root.right:
            self._dfs(root.right, res, False)
        return res[0]

    # return tuple (go_left, go_right)
    def _dfs(self, node, res, is_left_node):
        res_for_left_node = (0, 0)
        if node.left:
            res_for_left_node = self._dfs(node.left, res, True)
        res_for_right_node = (0, 0)
        if node.right:
            res_for_right_node = self._dfs(node.right, res, False)
        left_zig_zag = 1 + res_for_left_node[1]
        right_zig_zag = 1 + res_for_right_node[0]
        res[0] = max(res[0], left_zig_zag - int(is_left_node), right_zig_zag - int(not is_left_node))
        return (left_zig_zag, right_zig_zag)
        