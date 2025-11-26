class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
      mod = 10 ** 9 + 7
      m, n = len(grid), len(grid[0])
      counters = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
      cur_row = m - 1
      cur_col = n - 1
      counters[cur_row][cur_col][grid[cur_row][cur_col] % k] = 1

      while True:
        done = False
        next_row = cur_row - 1
        next_col = cur_col - 1
        right_counters = counters[cur_row][cur_col + 1]
        bottom_counters = counters[cur_row + 1][cur_col]
        for remainder in range(k):
          count_remainders_right = right_counters[remainder]
          count_remainders_bottom = bottom_counters[remainder]
          # print(cur_row, cur_col)
          counters[cur_row][cur_col][(remainder + grid[cur_row][cur_col]) % k] += (count_remainders_right + count_remainders_bottom) % mod
          
        for row in range(cur_row - 1, -1, -1):
          # print(row, cur_col + 1)
          right_counters = counters[row][cur_col + 1]
          bottom_counters = counters[row + 1][cur_col]
          for remainder in range(k):
            count_remainders_right = right_counters[remainder]
            count_remainders_bottom = bottom_counters[remainder]
            counters[row][cur_col][(remainder + grid[row][cur_col]) % k] += (count_remainders_right + count_remainders_bottom) % mod
          # print(row, cur_col)
          if row == 0 and cur_col == 0:
            done = True
            break
        for col in range(cur_col - 1, -1, -1):
          right_counters = counters[cur_row][col + 1]
          bottom_counters = counters[cur_row + 1][col]
          for remainder in range(k):
            count_remainders_right = right_counters[remainder]
            count_remainders_bottom = bottom_counters[remainder]
            counters[cur_row][col][(remainder + grid[cur_row][col]) % k] += (count_remainders_right + count_remainders_bottom) % mod
          # print(cur_row, col)
          if cur_row == 0 and col == 0:
            done = True
            break
        if (cur_row == 0 and cur_col == 0) or done:
            break
        cur_row = next_row
        cur_col = next_col
      # for i in range(m):
      #   print(counters[i][:-1])
      return counters[0][0][0]