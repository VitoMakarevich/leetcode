# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        store = {
            0: dummy_head
        }
        s = 0
        cursor = dummy_head
        deleted = True
        while deleted:
            deleted = False
            while cursor.next:
                s += cursor.next.val
                if not s in store:
                    store[s] = cursor.next
                    cursor = cursor.next
                else:
                    store[s].next = cursor.next.next
                    cursor = store[s]
                    del store[s]
                    deleted = True
                    break
            cursor = dummy_head
            s = 0
            store = {
                0: dummy_head
            }


        return dummy_head.next