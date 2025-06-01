class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
      nums = sorted(set(nums))
      res = 0
      prev = 0
      for num in nums:
        in_between = min(k, num - prev - 1)
        sum_between = (2 * (prev + 1) + in_between - 1) * in_between // 2
        res += sum_between
        k -= in_between
        if k == 0:
          return res
        prev = num
      res += (2 * (prev + 1) + k - 1) * k // 2
      return res

      
        
          
        