# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        iterator = head
        count = 0
        while iterator:
          count += 1
          iterator = iterator.next
        idx = 0
        res = [0] * count 
        q = deque()
        while head:
          while q and head.val > q[-1][1]:
            position, value = q.pop()
            res[position] = head.val
          q.append((idx, head.val))
          idx += 1
          head = head.next
        
        for idx, _ in q:
          res[idx] = 0
        
        return res