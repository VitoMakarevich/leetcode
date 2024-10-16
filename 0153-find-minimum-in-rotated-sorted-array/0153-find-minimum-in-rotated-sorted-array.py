class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = -1
        while True:
            mid = floor((right - left) / 2) + left
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                res = right
                break
            elif nums[left] > nums[right] and not nums[mid] > nums[left]:
                right = mid

            else:
                left = mid
        if res == len(nums) - 1:
            return nums[0]
        else:
            return nums[res + 1]