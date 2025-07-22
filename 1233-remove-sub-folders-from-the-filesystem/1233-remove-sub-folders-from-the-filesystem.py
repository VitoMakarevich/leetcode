class TrieNode:
  def __init__(self):
    self.childs = {}
    self.mentioned = False
  
  def mark_mentioned(self):
    self.mentioned = True
  
  def get_or_create_child(self, name):
    if not name in self.childs:
      self.childs[name] = TrieNode()
    return self.childs[name]
  

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for folder_parts in folder:
          cur = root
          for folder_name in folder_parts.split('/')[1:]:
            cur = cur.get_or_create_child(folder_name)
          cur.mark_mentioned()
        
        res = []
        path_so_far = []
        def dfs(node, name):
          path_so_far.append(name)
          if node.mentioned:
            res.append(f"{'/'.join(path_so_far)}")
          else:
            for child_name, child in node.childs.items():
              dfs(child, child_name)
          path_so_far.pop()

        dfs(root, '')
        return res