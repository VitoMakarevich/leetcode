# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = deque()
        iterator = head
        while iterator:
          stack.append(iterator)
          iterator = iterator.next
        new_head = head
        curr = head
        for _ in range(len(stack) // 2):
            next_node = curr.next
            tail_node = stack.pop()

            curr.next = tail_node
            tail_node.next = next_node
            curr = next_node

        curr.next = None
        return head
        
        # 1 -> 2 -> 3 -> 4
        # 4 -> 3 -> 2 -> 1

        # 1 -> 4 -> 2 -> 3