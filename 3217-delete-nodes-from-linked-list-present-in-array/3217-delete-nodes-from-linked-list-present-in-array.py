# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    num_to_del = set(nums)
    head = dummy.next
    prev = dummy
    while head:
      if head.val in num_to_del:
        prev.next = head.next
      else:
        prev = head
      head = head.next
      
    return dummy.next
