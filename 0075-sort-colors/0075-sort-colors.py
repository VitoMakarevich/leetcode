class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_white_blue = [0, 0, 0]
        for v in nums:
          red_white_blue[v] += 1
        index = 0
        for i in range(3):
          while index < len(nums) and red_white_blue[i] > 0:
            nums[index] = i
            index += 1
            red_white_blue[i] -= 1
        