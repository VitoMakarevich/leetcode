# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = defaultdict(list)
        self._dfs(root, duplicates)
        return [val[0] for _, val in duplicates.items() if len(val) > 1]
    def _dfs(self, root, duplicates):
        if not root:
            return
        serialized_node = self.serialize(root)
        duplicates[serialized_node].append(root)
        self._dfs(root.left, duplicates)
        self._dfs(root.right, duplicates)
    def serialize(self, node):
        if not node:
          return ""
        res = f"({self.serialize(node.left)}){node.val}({self.serialize(node.right)})"
        return res