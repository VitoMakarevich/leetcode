class Solution:
    def getSum(self, a: int, b: int) -> int:
      abs_a, abs_b = abs(a), abs(b)
      if abs_a < abs_b:
        return self.getSum(b, a)
      
      sign = 1 if a > 0 else -1

      if a * b >= 0:
        while abs_b:
          xor = abs_a ^ abs_b
          carry = (abs_a & abs_b) << 1
          abs_a = xor
          abs_b = carry
      else:
        while abs_b:
          xor = abs_a ^ abs_b
          borrow = ((~abs_a) & abs_b) << 1
          abs_a = xor
          abs_b = borrow
      return abs_a * sign