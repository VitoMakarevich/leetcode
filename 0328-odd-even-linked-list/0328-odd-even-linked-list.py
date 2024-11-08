# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        odd = head
        even = head.next
        even_first = even
        cur = head.next.next
        is_odd = True
        while cur:
            if is_odd:
                odd.next = cur
                odd = cur
            else:
                even.next = cur
                even = cur
            cur = cur.next
            is_odd = not is_odd
        odd.next = even_first
        even.next = None
        return head