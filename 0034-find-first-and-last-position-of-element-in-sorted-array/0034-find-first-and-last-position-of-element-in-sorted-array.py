class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self._internal_search(nums, target, 0, len(nums) - 1, True)
        right = self._internal_search(nums, target, 0, len(nums) - 1, False)
        return [left, right]

    def _internal_search(self, nums, target, left, right, find_leftmost):
        if left > right:
            return -1

        mid = left + floor((right - left) / 2)
        if nums[mid] > target:
            return self._internal_search(nums, target, left, mid - 1, find_leftmost)
        elif nums[mid] < target:
            return self._internal_search(nums, target, mid + 1, right, find_leftmost)
        else:
            if find_leftmost:
                another_to_the_left = self._internal_search(nums, target, left, mid - 1, find_leftmost)
                if another_to_the_left != -1:
                    return another_to_the_left
                else:
                    return mid
            else:
                another_to_the_right = self._internal_search(nums, target, mid + 1, right, find_leftmost)
                if another_to_the_right != -1:
                    return another_to_the_right
                else:
                    return mid