# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        store = {
        }
        s = 0
        cursor = dummy_head
        while cursor:
            s += cursor.val
            if not s in store:
                store[s] = cursor
            else:
                to_delete = store[s].next
                print(to_delete, s)
                temp_sum = s + to_delete.val
                while to_delete != cursor:
                    del store[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                store[s].next = cursor.next
                
            cursor = cursor.next

        return dummy_head.next