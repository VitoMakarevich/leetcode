class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        leftmost_same_bit = -1
        cp_left = left
        cp_right = right
        # find leftmost 1 in the same position
        # if there is no such - there will be no 1 bits at all
        while cp_left > 0 and cp_right > 0:
            cp_left >>= 1
            cp_right >>= 1
            leftmost_same_bit += 1

        # if there is no 1 bits at all(so no while iterations)
        # or numbers have 1s at different position - eventually AND will result in 0
        if (leftmost_same_bit == -1) or cp_left != cp_right:
            return 0
        cp_left = left
        cp_right = right
        rightmost_same_bit = leftmost_same_bit
        # go from leftmost_same bit and get rightmost same bit(can be 0 or 1, just by the same)
        while rightmost_same_bit -1 >= 0:
            temp = rightmost_same_bit - 1
            mask = 1 << temp
            bit_equals = (cp_left & mask) == (cp_right & mask) 
            if not bit_equals:
                break
            rightmost_same_bit = temp
        mask = ((1 << (leftmost_same_bit - rightmost_same_bit + 1)) - 1) << rightmost_same_bit
        return left & mask & right