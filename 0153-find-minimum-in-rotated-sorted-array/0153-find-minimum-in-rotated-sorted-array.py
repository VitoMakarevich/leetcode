class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = -1
        while True:
            mid = floor((right - left) / 2) + left
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                # print(f"found result at left={left}, mid={mid}, right={right}, res={right}")
                res = right
                break
            elif nums[left] > nums[right] and not nums[mid] > nums[left]:
                # print(f"moving to left at left={left}, mid={mid}, right={right}, new_right={mid - 1}")
                right = mid

            else:
                # print(f"moving to right at left={left}, mid={mid}, right={right}, new_right={mid + 1}")
                left = mid
        # print(res)
        # return res
        if res == len(nums) - 1:
            return nums[0]
        else:
            return nums[res + 1]