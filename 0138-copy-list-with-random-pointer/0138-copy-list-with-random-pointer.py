"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        iterator = head
        new_list_iterator = None
        mapping = {}
        while iterator:
          new_list_node = Node(iterator.val)
          if new_head is None:
            new_head = new_list_node
          mapping[iterator] = new_list_node
          
          if new_list_iterator is None:
            new_list_iterator = new_list_node
          else:
            new_list_iterator.next = new_list_node
            new_list_iterator = new_list_iterator.next

          iterator = iterator.next

        iterator = head
        new_list_iterator = new_head

        # for k, v in mapping.items():
        #   print(k.val, v.val)
        while iterator:
          if iterator.random:
            new_list_iterator.random = mapping[iterator.random]
          iterator = iterator.next
          new_list_iterator = new_list_iterator.next
        
        return new_head


