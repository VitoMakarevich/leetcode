class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = [{} for i in range(len(nums))]
        return self._dp(nums, 0, cache, 0, 0)

    def _dp(self, nums, cur_index, cache, left_sum, right_sum):
        if cur_index == len(nums) - 1:
            return abs(left_sum - right_sum) == nums[cur_index]
        if not left_sum in cache[cur_index]:
            if_to_left = self._dp(nums, cur_index + 1, cache, left_sum + nums[cur_index], right_sum)
            if_to_right = self._dp(nums, cur_index + 1, cache, left_sum, right_sum + nums[cur_index])
            cache[cur_index][left_sum] = if_to_left or if_to_right
        return cache[cur_index][left_sum]
            
        