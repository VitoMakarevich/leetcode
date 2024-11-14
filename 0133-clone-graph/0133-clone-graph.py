"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.nodes = {}
        if node is None:
          return None
        res = Node(node.val)
        self.nodes[node.val] = res
        self.dig(node, res, None)

        return res
        
    def dig(self, old_node, new_node, prev):
      for old_neighbor in old_node.neighbors:
        if not old_neighbor.val in self.nodes :
            nn = Node(old_neighbor.val, [new_node])
            self.nodes[nn.val] = nn
            self.nodes[new_node.val].neighbors.append(nn)
            self.dig(old_neighbor, nn, new_node)
            
        elif not prev or (prev and old_neighbor.val != prev.val):
            new_node.neighbors.append(self.nodes[old_neighbor.val])
            


