class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self._nums = nums
        self._target = target
        left = self._internal_search(0, len(nums) - 1, True)
        right = self._internal_search(0, len(nums) - 1, False)
        return [left, right]

    def _internal_search(self, left, right, find_leftmost):
        if left > right:
            return -1

        mid = left + floor((right - left) / 2)
        if self._nums[mid] > self._target:
            return self._internal_search(left, mid - 1, find_leftmost)
        elif self._nums[mid] < self._target:
            return self._internal_search(mid + 1, right, find_leftmost)
        else:
            next_copied = None
            if find_leftmost:
                next_copied = self._internal_search(left, mid - 1, find_leftmost)
            else:
                next_copied = self._internal_search(mid + 1, right, find_leftmost)
            return next_copied if next_copied != -1 else mid