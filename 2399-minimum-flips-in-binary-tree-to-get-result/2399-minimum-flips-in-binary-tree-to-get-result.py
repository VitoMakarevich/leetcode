# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
      return self._dp_cached({}, root, result)

    def _dp_cached(self, cache, root, needed_result):
        if root not in cache:
          cache[root] = [None, None]
        index = int(needed_result)
        if cache[root][index] is None:
          cache[root][index] = self._dp(cache, root, needed_result)
        return cache[root][index]

    def _dp(self, cache, root, needed_result):
      if root.val == 0 or root.val == 1:
        return int(not needed_result == bool(root.val))
      elif root.val == 2:
        if needed_result:
          left_count = self._dp_cached(cache, root.left, needed_result)
          if left_count == 0:
            return 0
          right_count = self._dp_cached(cache, root.right, needed_result)
          if right_count == 0:
            return 0
          return min(left_count, right_count)
        else:
          return self._dp_cached(cache, root.left, needed_result) + self._dp_cached(cache, root.right, needed_result)
      elif root.val == 3:
        if needed_result:
          left_count = self._dp_cached(cache, root.left, needed_result)
          right_count = self._dp_cached(cache, root.right, needed_result)
          return left_count + right_count
        else:
          left_count = self._dp_cached(cache, root.left, needed_result)
          if left_count == 0:
            return 0
          right_count = self._dp_cached(cache, root.right, needed_result)
          if right_count == 0:
            return 0
          return min(left_count, right_count)
      elif root.val == 4:
        candidates = []
        if needed_result:
          left_count = self._dp_cached(cache, root.left, True) + self._dp_cached(cache, root.right, False)
          if left_count == 0:
            return 0
          right_count = self._dp_cached(cache, root.left, False) + self._dp_cached(cache, root.right, True)
          if right_count == 0:
            return 0
          return min(left_count, right_count)
        else:
          left_count = self._dp_cached(cache, root.left, False) + self._dp_cached(cache, root.right, False)
          if left_count == 0:
            return 0
          right_count = self._dp_cached(cache, root.left, True) + self._dp_cached(cache, root.right, True)
          if right_count == 0:
            return 0
          return min(left_count, right_count)
      else:
        if root.left:
          return self._dp_cached(cache, root.left, not needed_result)
        else:
          return self._dp_cached(cache, root.right, not needed_result)