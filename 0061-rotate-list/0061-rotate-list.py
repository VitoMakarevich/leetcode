# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nxt = head 
        cnt = 0
        if head is None:
          return head
        while nxt is not None:
          cnt += 1
          nxt = nxt.next
        remainder = k % cnt
        if remainder == 0:
          return head
        
        # node to be the end - set .next to None
        # positioned at (length - k - 1), e.g. n = 5, k = 2, needed end will be at idx 2
        end_pos = cnt - remainder - 1

        # result pointer to head - one after end
        res_head_pos = cnt - remainder
        res = None

        # place where old-end and old-start concatenate
        # pointer to old-node end
        # positioned at the end and should point to old start
        scar = cnt - 1

        nxt = head
        counter = 0
        print(f"cnt={cnt}, remainder={remainder}, end_pos = {end_pos}, res_pos = {res_head_pos}, scar = {scar}")
        while nxt is not None:
          if counter == res_head_pos:
            res = nxt
            print(f"setting new result position {res.val}")
          if counter == scar:
            print(f"concatenating {nxt.val} and {head.val}")
            next_val = nxt.next
            nxt.next = head
            nxt = next_val
          elif counter == end_pos:
            print(f"setting next of {nxt.val} to None as it will be end")
            next_val = nxt.next
            nxt.next = None
            nxt = next_val
          else:
            nxt = nxt.next
          counter += 1
        
        return res



        

