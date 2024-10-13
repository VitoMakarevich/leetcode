class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow_bit = False
        for index in reversed(range(len(digits))):
            value = digits[index]
            if index == len(digits) - 1:
                if value == 9:
                    overflow_bit = True
                    digits[index] = 0
                else:
                    digits[index] += 1
            elif overflow_bit:
                if value == 9:
                    overflow_bit = True
                    digits[index] = 0
                else:
                    digits[index] += 1
                    overflow_bit = False
        
        if overflow_bit:
            digits.insert(0, 1)
        
        return digits