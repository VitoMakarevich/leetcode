class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
      stack = []
      stack.append(nums[0])
      idx = 1
      num_size = len(nums)

      while idx < len(nums):
        non_coprime = gcd(nums[idx], stack[-1]) > 1
        if non_coprime:
          stack.append(lcm(stack.pop(), nums[idx]))
        else:
          stack.append(nums[idx])
        idx += 1
        while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
          stack.append(lcm(stack.pop(), stack.pop()))

      return stack

