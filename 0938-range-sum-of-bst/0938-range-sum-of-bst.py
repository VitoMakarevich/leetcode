# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            local_res = 0
            if low <= node.val <= high:
                print(f'adding {node.val}')
                local_res += node.val
            if node.left and (node.left.val >= low or node.val > low):
                local_res += dfs(node.left)
            if node.right and (node.right.val <= high or node.val < high):
                local_res += dfs(node.right)
            return local_res
        return dfs(root)
            