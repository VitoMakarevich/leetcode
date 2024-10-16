class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        biggest_pos = -1
        while True:
            mid = floor((right - left) / 2) + left
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                biggest_pos = right
                break
            elif nums[left] > nums[right] and not nums[mid] > nums[left]:
                right = mid
            else:
                left = mid

        if biggest_pos == len(nums) - 1:
            return self._find(0, len(nums) - 1, target, nums)
        else:
            left_search = self._find(0, biggest_pos, target, nums)
            if left_search == -1:
                return self._find(biggest_pos + 1, len(nums) - 1, target, nums)
            else:
                return left_search

    
    def _find(self, left, right, target, nums):
        while left <= right:
            mid = floor((right - left) / 2) + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        