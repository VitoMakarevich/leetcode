# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"), head)
        pointer = dummy.next
        sorted_end = dummy
        while pointer:
            nxt = pointer.next
            if pointer.val > sorted_end.val:
                sorted_end.next = pointer
                pointer.next = None
                sorted_end = pointer
            else:
                iterator = dummy
                while iterator.next and iterator.next.val < pointer.val:
                    if iterator == sorted_end:
                        break
                    iterator = iterator.next
                tmp_iterator_next = iterator.next
                iterator.next = pointer
                pointer.next = tmp_iterator_next
            pointer = nxt
        return dummy.next