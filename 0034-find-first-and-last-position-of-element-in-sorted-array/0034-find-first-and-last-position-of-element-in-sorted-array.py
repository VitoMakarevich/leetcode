class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self._nums = nums
        self._target = target
        return self.search_with_loop(nums, target)

    def search_with_loop(self, nums, target):
        any_coordinate = self._any_match(0, len(nums) - 1)
        if any_coordinate == -1:
            return [-1, -1]
        else:
            right_border = any_coordinate
            while right_border + 1 < len(nums) and nums[right_border + 1] == target:
                right_border += 1
            left_border = any_coordinate
            while left_border - 1 >= 0 and nums[left_border - 1] == target:
                left_border -= 1
            return [left_border, right_border]

    def _any_match(self, left, right):
        if left > right:
            return -1

        mid = left + floor((right - left) / 2)
        if self._nums[mid] == self._target:
            return mid
        if self._nums[mid] > self._target:
            return self._any_match(left, mid - 1)
        else:
            return self._any_match(mid + 1, right)

    def _search_pure_log(self, nums, target):
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