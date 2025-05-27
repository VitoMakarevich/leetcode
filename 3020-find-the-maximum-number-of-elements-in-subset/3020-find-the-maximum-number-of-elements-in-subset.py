class Solution:
    def maximumLength(self, nums: List[int]) -> int:
      counter = Counter(nums)
      nums.sort()
      visited = set()
      res = 0
      for num in nums:
        if num in visited:
          continue
        if num == 1:
          res = max(res, 1)
          continue
        visited.add(num)
        prev_num = num
        cur_count = 1
        next_num = prev_num * prev_num
        while next_num in counter and counter[prev_num] > 1:
          visited.add(next_num)
          cur_count += 2
          temp = next_num
          
          prev_num, next_num = next_num, next_num * next_num
        res = max(res, cur_count)
      return res