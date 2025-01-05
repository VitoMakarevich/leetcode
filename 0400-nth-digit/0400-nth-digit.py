class Solution:
    def findNthDigit(self, n) -> List[int]:
        number_of_digits = 1
        count_of_digits_with_this_number_of_digits = 9 * pow(10, number_of_digits - 1)
        count_of_total_digits = count_of_digits_with_this_number_of_digits * number_of_digits
        while n - count_of_total_digits > 0:
            n -= count_of_total_digits
            number_of_digits += 1
            count_of_digits_with_this_number_of_digits = 9 * pow(10, number_of_digits - 1)
            count_of_total_digits = count_of_digits_with_this_number_of_digits * number_of_digits
        n -= 1
        digit_position = n // number_of_digits
        position_in_number = n % number_of_digits if number_of_digits > 1 else 0
        result_number = pow(10, number_of_digits - 1) + digit_position
        
        return int(str(result_number)[position_in_number])