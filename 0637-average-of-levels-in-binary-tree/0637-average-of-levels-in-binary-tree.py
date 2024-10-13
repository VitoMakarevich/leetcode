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
            c = len(queue)
            for i in range(c):
                item = queue.popleft()
                s += item.val
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            avg = s / c
            res.append(self.floor_to_5_places(avg))

        return res

    def floor_to_5_places(self, number):
        factor = 10 ** 5
        return math.floor(number * factor) / factor            