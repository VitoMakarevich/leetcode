class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
          mid = (left + right) // 2
          if nums[mid] > nums[-1]:
            left = mid + 1
          else:
            right = mid
        lowest_element = left
        biggest_element = lowest_element - 1 if lowest_element > 0 else len(nums) - 1
        found_in_smaller_array = self._search(nums, lowest_element, len(nums) - 1, target)
        if found_in_smaller_array == -1:
          return self._search(nums, 0, biggest_element, target)
        return found_in_smaller_array
    def _search(self, nums, left, right, target):
      while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
          return mid
        elif nums[mid] > target:
          right = mid - 1
        else:
          left = mid + 1
      return -1