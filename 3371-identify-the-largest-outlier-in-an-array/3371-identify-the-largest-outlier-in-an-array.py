class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        count = Counter(nums)
        total_sum = sum(nums)
        largest = -inf
        for n in nums:
          sum_without_this = total_sum - n
          count[n] -= 1
          sum_element = sum_without_this / 2
          if sum_element in count and count[sum_element] > 0:
            largest = max(largest, n)
          count[n] += 1
        return largest