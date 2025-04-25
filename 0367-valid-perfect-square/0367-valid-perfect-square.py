class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num // 2
        while low <= high:
          mid = (low + high) // 2
          candidate = mid * mid
          if candidate == num:
            return True
          elif candidate > num:
            high = mid - 1
          else:
            low = mid + 1
        return False if num != 1 else True
