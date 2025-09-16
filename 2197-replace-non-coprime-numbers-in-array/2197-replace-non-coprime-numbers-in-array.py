class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
      stack = []
      stack.append(nums[0])
      idx = 1
      num_size = len(nums)

      @cache
      def c_gcd(a, b):
        return gcd(a, b)
      @cache
      def c_lcm(a, b):
        return lcm(a, b)
      while idx < len(nums):
        non_coprime = c_gcd(nums[idx], stack[-1]) > 1
        if non_coprime:
          stack.append(c_lcm(stack.pop(), nums[idx]))
        else:
          stack.append(nums[idx])
        idx += 1
        while len(stack) >= 2 and c_gcd(stack[-1], stack[-2]) > 1:
          stack.append(c_lcm(stack.pop(), stack.pop()))

      return stack

