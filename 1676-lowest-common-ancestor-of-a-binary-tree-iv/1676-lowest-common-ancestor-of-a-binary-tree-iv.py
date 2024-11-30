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
        p = []
        res_path = []
        self._dfs(p, res_path, seek_nodes, root)
        return res_path[0][-1]
        

    def _dfs(self, cur_path, res_path, seek_nodes, cur_node):
      cur_path.append(cur_node)
      if cur_node.val in seek_nodes:
        seek_nodes.remove(cur_node.val)
        if len(res_path) == 0:
          res_path.append(cur_path.copy())
        else:
          i = 0
          while i < len(res_path[0]) and i < len(cur_path) and cur_path[i].val == res_path[0][i].val:
            i += 1
          res_path[0] = res_path[0][0: i]
      if len(seek_nodes) == 0:
        return
      if cur_node.left:
        self._dfs(cur_path, res_path, seek_nodes, cur_node.left)
      if len(seek_nodes) == 0:
        return
      if cur_node.right:
        self._dfs(cur_path, res_path, seek_nodes, cur_node.right)
      if len(seek_nodes) == 0:
        return
      cur_path.pop()