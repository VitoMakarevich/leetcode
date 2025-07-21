# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
      plain_list = []
      while head is not None:
        plain_list.append(head.val)
        head = head.next
      root = self._dfs(0, len(plain_list) - 1, plain_list)
      return root
    def _dfs(self, left, right, s_list):
      if left > right:
        return None
      mid = (left + right) // 2
      node = TreeNode(s_list[mid])
      node.left = self._dfs(left, mid - 1, s_list)
      node.right = self._dfs(mid + 1, right, s_list)
      return node