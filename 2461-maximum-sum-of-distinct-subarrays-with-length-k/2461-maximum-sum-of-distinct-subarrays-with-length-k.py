class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = set()
        res = 0
        sum_s = 0
        for i, n in enumerate(nums):

          if len(s) < k and not n in s:
            s.add(n)
            sum_s += n
            if len(s) == k:
              res = max(res, sum_s)
          elif len(s) == k and not n in s:
            last = nums[i - k]
            s.remove(last)
            sum_s -= last
            s.add(n)
            sum_s += n
            res = max(res, sum_s)
          else:
            last = i - len(s)
            while nums[last] != n:
              s.remove(nums[last])
              sum_s -= nums[last]
              last += 1
            

        return res
        