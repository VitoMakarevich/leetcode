class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        non_zero_pointer = 0
        while zero_pointer < len(nums) and non_zero_pointer < len(nums):
            while zero_pointer < len(nums) and nums[zero_pointer] != 0:
                zero_pointer += 1
            while non_zero_pointer < len(nums) and nums[non_zero_pointer] == 0:
                non_zero_pointer += 1
            # print(zero_pointer, non_zero_pointer)
            if zero_pointer < len(nums) and non_zero_pointer < len(nums):
                if zero_pointer < non_zero_pointer:
                    nums[zero_pointer], nums[non_zero_pointer] = nums[non_zero_pointer], nums[zero_pointer]
                    zero_pointer += 1
                    non_zero_pointer += 1
                else:
                    non_zero_pointer += 1

        