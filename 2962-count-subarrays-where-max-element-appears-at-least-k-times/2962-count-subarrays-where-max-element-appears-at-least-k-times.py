class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        max_indexes = []
        ans = 0
        for index, v in enumerate(nums):
            if v == max_element:
              max_indexes.append(index)
            count = len(max_indexes)
            if count >= k:
              ans += max_indexes[-k] + 1
        return ans