# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        seek_nodes = set()
        for node in nodes:
          seek_nodes.add(node.val)
        cur = root
        p = deque()
        paths = deque()
        self._dfs(p, paths, seek_nodes, root)
        last_popped = None
        while min(map(len, paths)) > 0 and len(set(map(lambda x: x[0].val, paths))) == 1:
          for local_path in paths:
            last_popped = local_path.popleft()
        
        return last_popped
        

    def _dfs(self, cur_path, paths, seek_nodes, cur_node):
      cur_path.append(cur_node)
      if cur_node.val in seek_nodes:
        paths.append(cur_path.copy())
      if len(paths) == len(seek_nodes):
        return
      if cur_node.left:
        self._dfs(cur_path, paths, seek_nodes, cur_node.left)
      if cur_node.right:
        self._dfs(cur_path, paths, seek_nodes, cur_node.right)
      cur_path.pop()