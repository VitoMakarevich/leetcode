class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = [0] * 101
        mx = 0
        for birth, death in logs:
          line[birth - 1950] += 1
          line[death - 1950] -= 1
        cur = line[0]
        cur_max = line[0]
        max_year = 0
        for idx, change in enumerate(line):
          cur += change
          if cur > cur_max:
            cur_max = cur
            max_year = idx
        return max_year + 1950