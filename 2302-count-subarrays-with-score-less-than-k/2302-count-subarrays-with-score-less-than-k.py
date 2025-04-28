class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for v in nums:
          prefix_sum.append(v + prefix_sum[-1])
        res = 0
        for index, value in enumerate(nums):
          last_index = self.bisect_left(prefix_sum, k, index)
          res += last_index - index + 1
        return res
    
    def bisect_left(self, prefix_sum, k, start):
      low = start
      high = len(prefix_sum) - 1
      ans = start - 1
      while low < high:
        mid = (low + high) // 2
        sum_between = self.sum_from_to(prefix_sum, start, mid)
        distance = mid - start + 1
        if sum_between * distance < k:
          ans = mid
          low = mid + 1
        else:
          high = mid
      return ans
    
    def sum_from_to(self, prefix_sum, start, end):
      return prefix_sum[end + 1] - prefix_sum[start]