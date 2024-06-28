# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_smaller = ListNode()
        smaller = dummy_smaller
        dummy_bigger = ListNode()
        bigger = dummy_bigger

        nxt = head
        while nxt:
          if nxt.val < x:
            smaller.next = ListNode(nxt.val)
            smaller = smaller.next
          else:
            bigger.next = ListNode(nxt.val)
            bigger = bigger.next
          nxt = nxt.next
        
        smaller.next = dummy_bigger.next
      
        return dummy_smaller.next

            