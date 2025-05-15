class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
      min_v, max_v = 0, -inf
      for v in arr:
        max_v = max(max_v, v)
      low, high = min_v, max_v
      res = max_v
      ans = 0
      while low < high:
        mid = (low + high) // 2
        arr_sum = self.sum(arr, mid)
        
        if arr_sum > target:
          high = mid
        else:
          low = mid + 1
      sum_low = self.sum(arr, low)
      sum_low_minus = self.sum(arr, low - 1)

      if abs(sum_low - target) < abs(sum_low_minus - target):
          return low
      else:
          return low - 1


    def sum(self, arr, cap):
      return sum([v if v < cap else cap for v in arr])