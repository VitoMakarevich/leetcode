class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        queue = deque()
        res = [0] * len(nums)
        for index in range(len(nums)):
          while queue and nums[index] > nums[queue[-1]]:
            last_idx = queue.pop()
            res[last_idx] = nums[index]
          queue.append(index)

        for index in range(len(nums)):
          while queue and nums[index] > nums[queue[-1]]:
            last_idx = queue.pop()
            res[last_idx] = nums[index]

        for idx in queue:
          res[idx] = -1
        return res
