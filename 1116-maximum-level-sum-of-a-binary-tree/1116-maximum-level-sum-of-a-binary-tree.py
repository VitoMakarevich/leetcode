# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])
        lvl = 1
        max_sum = float('-inf')
        max_sum_lvl = 1
        while bfs:
            local_sum = 0
            for i in range(len(bfs)):
                nxt = bfs.popleft()
                local_sum += nxt.val
                if nxt.left:
                    bfs.append(nxt.left)
                if nxt.right:
                    bfs.append(nxt.right)
            if local_sum > max_sum:
                max_sum = local_sum
                max_sum_lvl = lvl
            lvl += 1
        
        return max_sum_lvl