class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = 0
        while num2 > 0:
          set_bits += num2 & 1
          num2 >>= 1
        
        bit_check = 31
        res = 0
        
        for i in range(31, -1, -1):
          if 1 << i & num1 and set_bits > 0:
            res = res | 1 << i
            set_bits -= 1
        idx = 0
        while set_bits > 0:
          if 1 << idx & res == 0:
            res = res | 1 << idx
            set_bits -= 1
          idx += 1
        return res


