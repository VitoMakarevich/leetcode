# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        dummy = ListNode()
        dummy.next = head

        nxt = dummy
        index = 1
        while nxt is not None and index < left:
          nxt = nxt.next
          index += 1
        
        last_normal = nxt
        d = deque()
        while index <= right:
            nxt = nxt.next
            index += 1
            d.appendleft(nxt.val)
        
        normal_continue = nxt.next

        while len(d) > 0:
            next_item_reverse = d.popleft()
            new_node = ListNode(val = next_item_reverse)
            last_normal.next = new_node
            last_normal = new_node

        last_normal.next = normal_continue

        return dummy.next
        

