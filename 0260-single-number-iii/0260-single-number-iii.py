class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
      num = 0
      for n in nums:
        num ^= n
      last_set_bit = num & (-num)
      mask = 0
      for n in nums:
        if n & last_set_bit != 0:
          mask ^= n

      return [mask, mask ^ num]