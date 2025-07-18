class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        total_missing = arr[-1] - len(arr)
        left = 0
        right = len(arr) - 1
        def missing_to_left(pos):
          return arr[pos] - pos - 1
        while left < right:
          mid = (left + right) // 2
          mtl = missing_to_left(mid)
          if mtl >= k:
            right = mid
          else:
            left = mid + 1
        missing_from_right = missing_to_left(left)
        if left == 0:
          if missing_from_right < k:
            return arr[left] + k - missing_from_right
          else:
            return k
        elif k > missing_from_right:
          return arr[left] + k - missing_from_right
        else:
          prev = missing_to_left(left - 1)
          to_add = k - prev
          return arr[left - 1] + to_add