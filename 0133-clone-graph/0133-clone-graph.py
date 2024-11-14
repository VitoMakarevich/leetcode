"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    nodes = []
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.nodes = {}
        self.visited = set()
        if node is None:
          return None
        res = Node(node.val)
        self.nodes[node.val] = res
        self.dig(node, res, None)

        # vis = set()
        # self.log(res, vis)
        return res
        
    def log(self, root, vis):
      vis.add(root.val)
      print(vis)
      print(f"for node {root.val} neighbours are {list(map(lambda x: x.val, root.neighbors))}")
      for neighbor in [n for n in root.neighbors if not n.val in vis]:
        self.log(neighbor, vis)

    def dig(self, old_node, new_node, prev):
      for old_neighbor in old_node.neighbors:
        if not old_neighbor.val in self.nodes :
            nn = Node(old_neighbor.val, [new_node])
            self.nodes[nn.val] = nn
            self.nodes[new_node.val].neighbors.append(nn)
            self.dig(old_neighbor, nn, new_node)
            
        elif not prev or (prev and old_neighbor.val != prev.val):
            new_node.neighbors.append(self.nodes[old_neighbor.val])
            # print(f"adding neighbor {old_neighbor.val} into {new_node.val} at {new_node.val}")
            


