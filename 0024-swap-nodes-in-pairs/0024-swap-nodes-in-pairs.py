# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        new_start = None
        while cur:
            prev_copy = cur
            next_iteration = cur.next.next if cur.next else None
            new_cur = cur
            if cur.next:
                next_copy = cur.next
                cur.next = None
                next_copy.next = cur
                new_cur = next_copy
                if new_start is None:
                    new_start = new_cur
            if prev:
                prev.next = new_cur
            prev = new_cur.next
            cur = next_iteration
        return new_start if new_start else head
