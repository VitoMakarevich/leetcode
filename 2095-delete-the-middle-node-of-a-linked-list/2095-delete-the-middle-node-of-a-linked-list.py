# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_slow = None
        slow = head
        fast = head.next
        if not fast:
            return None
        while slow and fast:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next if fast.next else None
        prev_slow.next = slow.next
        return head