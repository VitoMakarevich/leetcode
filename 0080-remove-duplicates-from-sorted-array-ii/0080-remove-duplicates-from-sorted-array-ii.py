class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i = 0
      cnt = 0
      while i < len(nums):
        # print(f"iterating idx {i}, cnt {cnt}")
        duplicates_start = i
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
          j += 1
        duplicates_end = j - 1
        # print(f"for val {nums[i]}, duplicates are in range [{duplicates_start}, {duplicates_end}]")
        if duplicates_end != duplicates_start:
          nums[cnt] = nums[i]
          nums[cnt + 1] = nums[i]
          cnt += 2
          i = j
        else:
          nums[cnt] = nums[i]
          cnt += 1
          i += 1
      return cnt
