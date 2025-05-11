# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
      dir_path_to_start = deque()
      node_path_to_start = deque()
      path_to_start = self._path_to_node(root, dir_path_to_start, node_path_to_start, startValue)
      dir_path_to_end = deque()
      node_path_to_end = deque()
      path_to_end = self._path_to_node(root, dir_path_to_end, node_path_to_end, destValue)
      node_path_to_start.popleft()
      node_path_to_end.popleft()
      while node_path_to_start and node_path_to_end and node_path_to_start[0] == node_path_to_end[0]:
        node_path_to_start.popleft()
        node_path_to_end.popleft()
        dir_path_to_end.popleft()
        dir_path_to_start.popleft()

      res = 'U' * len(dir_path_to_start) + "".join(dir_path_to_end)
      return res
    
    def _path_to_node(self, root, dir_path, value_path, target):
      if not root:
        return False
      value_path.append(root.val)
      if root.val == target:
        return True
      dir_path.append("L")
      res = self._path_to_node(root.left, dir_path, value_path, target)
      if res:
        return True
      dir_path.pop()
      dir_path.append("R")
      res = self._path_to_node(root.right,dir_path, value_path, target)
      if res:
        return True
      dir_path.pop()
      value_path.pop()
      return False