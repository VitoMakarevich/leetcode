# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      if len(lists) == 0:
        return None
      return self._mergeKLists(lists, 0, len(lists) - 1)

    def _mergeKLists(self, lists, start, end):
      mid = ((end - start) // 2 + start)
      if start < end:
        left = self._mergeKLists(lists, start, mid)
        right = self._mergeKLists(lists, mid + 1, end)
        return self._mergeTwoLists(left, right)
      else:
        return lists[end]

        
    def _mergeTwoLists(self, left, right):
      if not left and not right:
        return None
      next_left = left
      next_right = right

      new_top_merged = None
      current_merged = None

      new_node = None
      if not next_right or (next_left and next_left.val < next_right.val):
        new_node = next_left
        next_left = next_left.next
      else:
        new_node = next_right
        next_right = next_right.next
      
      new_top_merged = new_node
      current_merged = new_node

      while next_left and next_right:
        new_node = None
        if next_left.val < next_right.val:
          new_node = next_left
          next_left = next_left.next
        else:
          new_node = next_right
          next_right = next_right.next
        
        current_merged.next = new_node
        current_merged = new_node

      if next_left and not next_right:
        current_merged.next = next_left
      else:
        current_merged.next = next_right

      return new_top_merged

