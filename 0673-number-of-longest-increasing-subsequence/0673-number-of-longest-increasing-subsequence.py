class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      if not nums:
        return 0
      lengths = [1] * len(nums)
      counts = [1] * len(nums)

      for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
          if nums[right] > nums[left]:
            taken_length = lengths[left] + 1
            not_taken_length = lengths[right]
            if taken_length > not_taken_length:
              lengths[right] = taken_length
              counts[right] = counts[left] 
            elif taken_length == not_taken_length:
              lengths[right] = taken_length
              counts[right] += counts[left]
      
      max_length = max(lengths)
      return sum(count for length, count in zip(lengths, counts) if length == max_length)
