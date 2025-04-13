class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()

        line = [0] * 102
        for start, end in nums:
          line[start] += 1
          line[end + 1] -= 1
        
        running_count = 0
        output = 0
        for p in range(1, 101):
          running_count += line[p]
          output += running_count != 0
        return output