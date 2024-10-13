class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self._nums = nums
        self._target = target
        return self._search_pure_log(nums, target)

    def _search_pure_log(self, nums, target):
        return self._internal_search(0, len(nums) - 1)
    def _internal_search(self, left, right):
        if left > right:
            return [-1, -1]

        mid = left + floor((right - left) / 2)
        if self._nums[mid] > self._target:
            return self._internal_search(left, mid - 1)
        elif self._nums[mid] < self._target:
            return self._internal_search(mid + 1, right)
        else:
            leftmost = min(self._internal_search(left, mid - 1))
            rightmost = max(self._internal_search(mid + 1, right))
            left_correct = leftmost if leftmost != -1 else mid
            right_correct = rightmost if rightmost != -1 else mid
            return [left_correct, right_correct]