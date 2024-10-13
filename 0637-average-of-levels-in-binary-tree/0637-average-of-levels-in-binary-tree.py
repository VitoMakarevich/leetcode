# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            this_level = []
            next_nodes = deque()
            while queue:
                item = queue.pop()
                this_level.append(item.val)
                if item.left:
                    next_nodes.append(item.left)
                if item.right:
                    next_nodes.append(item.right)
            avg = sum(this_level) / len(this_level)
            res.append(avg)
            while next_nodes:
                queue.append(next_nodes.pop())

        return res
            