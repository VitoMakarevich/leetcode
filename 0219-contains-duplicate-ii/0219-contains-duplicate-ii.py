class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      if k == 0:
        return False
      sliding_window = {}
      # for each step - check for previous occurence of this number
      #   yes - check length diff and return early if <= k
      # add index into window
      # if index >= k:
      # remove last seen index of value at index - k
      for index, value in enumerate(nums):
        if value in sliding_window and index - sliding_window[value] <= k:
          return True
        if index >= k:
          del sliding_window[nums[index - k]]
        sliding_window[value] = index
      return False
          