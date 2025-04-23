# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        levels = defaultdict(list)

        min_col, max_col = 0, 0
        queue = deque()
        queue.append((root, 0))
        
        while queue:
          for _ in range(len(queue)):
            cur_node, column = queue.popleft()
            levels[column].append(cur_node.val)
            min_col = min(min_col, column)
            max_col = max(max_col, column)

            if cur_node.left:
              queue.append((cur_node.left, column - 1))
            if cur_node.right:
              queue.append((cur_node.right, column + 1))
        
        return [levels[column] for column in range(min_col, max_col + 1)]
