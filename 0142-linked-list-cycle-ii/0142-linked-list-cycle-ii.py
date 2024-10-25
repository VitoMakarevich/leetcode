# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next.next if head and head.next else None
        fast_prev = head
        left_visited = set()
        while slow and fast:
            left_visited.add(slow)
            if fast in left_visited:
                break
            slow = slow.next
            fast_prev = fast
            fast = fast.next.next if fast.next else None
            
        if slow is None or fast is None:
            return None
        if fast_prev.next in left_visited:
            return fast_prev.next
        return fast
    