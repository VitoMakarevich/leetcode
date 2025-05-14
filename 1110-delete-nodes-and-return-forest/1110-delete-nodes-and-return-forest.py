class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
      res = []
      to_delete_set = set(to_delete)
      root = self.dfs(root, to_delete, res)
      if root:
        res.append(root)
      return res

    def dfs(self, node, to_delete, res):
      if not node:
        return None
      result_left_node = self.dfs(node.left, to_delete, res)
      result_right_node = self.dfs(node.right, to_delete, res)
      
      if node.val in to_delete:
        if result_left_node:
          res.append(result_left_node)
        if result_right_node:
          res.append(result_right_node)
        return None
      else:
        node.left = result_left_node
        node.right = result_right_node
        return node

     
      
