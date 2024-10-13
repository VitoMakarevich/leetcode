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
            s = 0
            c = 0
            next_nodes = deque()
            while queue:
                item = queue.pop()
                s += item.val
                c += 1
                if item.left:
                    next_nodes.append(item.left)
                if item.right:
                    next_nodes.append(item.right)
            avg = s / c
            res.append(self.floor_to_5_places(avg))
            queue = next_nodes

        return res

    def floor_to_5_places(self, number):
        factor = 10 ** 5
        return math.floor(number * factor) / factor            