"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
# idea:
# maintain cur and next and advance them
# if cur <= insert and (insert <= next or insert >= next) - insert in between and return head 
# Possible cases:
# head is None - return new node
# (cur <= insert <= next or cur >= next) - insert in between and return head 

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        cur, nxt = head, head.next
        while nxt.val >= cur.val and nxt != head:
          cur, nxt = cur.next, nxt.next
        lowest_value = nxt
        if insertVal < lowest_value.val:
          new_node.next = lowest_value
          cur.next = new_node
          return head
        
        cur, nxt = lowest_value, lowest_value.next
        while nxt.val < insertVal:
          cur, nxt = cur.next, nxt.next
        cur.next = new_node
        new_node.next = nxt

        return head