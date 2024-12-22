# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        return self._dp({}, root, result)

    def _dp(self, cache, root, needed_result):
      if not root in cache or not needed_result in cache[root]:
        if not root in cache:
          cache[root] = {}
        if not needed_result in cache[root]:
          if root.val == 0 or root.val == 1:
            cache[root][needed_result] = int(not needed_result == bool(root.val))
          elif root.val == 2:
            if needed_result:
              left_count = self._dp(cache, root.left, needed_result)
              right_count = self._dp(cache, root.right, needed_result)
              cache[root][needed_result] = min(left_count, right_count)
            else:
              cache[root][needed_result] = self._dp(cache, root.left, needed_result) + self._dp(cache, root.right, needed_result)
          elif root.val == 3:
            if needed_result:
              left_count = self._dp(cache, root.left, needed_result)
              right_count = self._dp(cache, root.right, needed_result)
              cache[root][needed_result] = left_count + right_count
            else:
              cache[root][needed_result] = min(self._dp(cache, root.left, needed_result), self._dp(cache, root.right, needed_result))
          elif root.val == 4:
            if needed_result:
              if_10 = self._dp(cache, root.left, True) + self._dp(cache, root.right, False)
              if_01 = self._dp(cache, root.left, False) + self._dp(cache, root.right, True)
              cache[root][needed_result] = min(if_10, if_01)
            else:
              if_00 = self._dp(cache, root.left, False) + self._dp(cache, root.right, False)
              if_11 = self._dp(cache, root.left, True) + self._dp(cache, root.right, True)
              cache[root][needed_result] = min(if_00, if_11)
          else:
            if root.left:
              cache[root][needed_result] = self._dp(cache, root.left, not needed_result)
            else:
              cache[root][needed_result] = self._dp(cache, root.right, not needed_result)

      return cache[root][needed_result]