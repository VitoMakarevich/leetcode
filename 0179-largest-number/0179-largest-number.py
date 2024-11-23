from functools import cmp_to_key
class Solution:
    def compare(self, x, y):
        pos = 0
        min_len = min(len(x), len(y))
        while pos < min_len:
            x_val = x[pos]
            y_val = y[pos]
            if x_val < y_val:
                return 1
            elif x_val > y_val:
                return -1
            pos += 1
        left_right = str(x) + str(y)
        right_left = str(y) + str(y)
        if left_right > right_left:
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:

        str_nums = list(map(lambda x: str(x), nums))
        sorted_nums = sorted(str_nums, key=cmp_to_key(self.compare))
        res = ''.join(sorted_nums)
        if res[0] == '0':
            return '0'

        return res
