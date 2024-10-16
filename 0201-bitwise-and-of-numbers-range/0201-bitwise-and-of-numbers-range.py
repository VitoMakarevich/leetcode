class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        counter = 0
        cp_left = left
        cp_right = right
        while cp_left > 0 and cp_right > 0:
            cp_left >>= 1
            cp_right >>= 1
            counter += 1

        leftmost_same_bit = counter - 1
        # print(f"cp_left={bin(cp_left)}, cp_right={bin(cp_right)}, leftmost_same_bit={leftmost_same_bit}")
        if leftmost_same_bit == 0 and cp_left == 0 and cp_right == 0:
            return 1 & left & right
        elif (cp_left != 0 or cp_right != 0):
            return 0
        elif leftmost_same_bit == -1:
            return 0
        cp_left = left
        cp_right = right
        rightmost_same_bit = leftmost_same_bit
        while rightmost_same_bit -1 >= 0:
            temp = rightmost_same_bit - 1
            mask = 1 << temp
            bit_equals = (cp_left & mask) == (cp_right & mask) 
            if not bit_equals:
                break
            rightmost_same_bit = temp
        # print(f"leftmost_same_bit={leftmost_same_bit} and rightmost_same_bit={rightmost_same_bit}")
        mask = ((1 << (leftmost_same_bit - rightmost_same_bit + 1)) - 1) << rightmost_same_bit
        # print(f"mask={bin(mask)}")
        return left & mask & right