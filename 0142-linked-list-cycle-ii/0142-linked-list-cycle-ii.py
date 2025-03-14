# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if fast == slow:
                break
        if slow is None or fast is None:
            return None

        left = head
        right = slow
        while left != right:
            left = left.next
            right = right.next

        return left
    