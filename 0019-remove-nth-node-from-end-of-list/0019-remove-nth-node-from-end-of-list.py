# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        front = None

        for i in range(1,n+1):
            fast = fast.next

        if fast == None:
            return head.next
            
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
