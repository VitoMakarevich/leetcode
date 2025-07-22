class Node:
  EMPTY_HASH = ''
  def __init__(self, name):
    self.childs = {}
    self.name = name
    self._hash = None
  
  def get_child(self, name):
    node = Node(name)
    if not name in self.childs:
      self.childs[name] = node
    return self.childs[name]
  
  def hash(self):
    if self._hash:
        return self._hash

    if not self.childs:
        return Node.EMPTY_HASH
    else:
        children_serials = []
        for name in self.childs:
            child = self.childs[name]
            children_serials.append(f"{name}({child.hash()})")
        self._hash = ''.join(children_serials)

    return self._hash

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node('/')
        paths.sort()

        for p in paths:
          cur_insert = root
          for path_part in p:
            cur_insert = cur_insert.get_child(path_part)
        
        store = defaultdict(list)
        def dfs_hash(node):
          hash_value = node.hash()
          store[hash_value].append(node)
          for ch in node.childs.values():
            dfs_hash(ch)
          
        dfs_hash(root)
        
        to_delete = {}
        for hash_value, nodes in store.items():
          if len(nodes) > 1 and not hash_value == Node.EMPTY_HASH:
            to_delete[hash_value] = nodes

        res = []
        def dfs_list(node, cur_path):
          cur_path.append(node.name)
          if not node.hash() in to_delete:
            res.append(list(cur_path))
            for child in node.childs.values():
              dfs_list(child, cur_path)
          cur_path.pop()
        for child in root.childs.values():
          dfs_list(child, [])
        return res

