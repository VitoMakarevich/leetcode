class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
      rows, cols = len(grid), len(grid[0])
      @cache
      def is_a_path(x, y, path_sum):
        cur_price = -1 if grid[x][y] == 0 else 1
        if x == rows - 1 and y == cols - 1:
          return path_sum + cur_price == 0
        else:
          return (x + 1 < rows and is_a_path(x + 1, y, path_sum + cur_price)) or (
            y + 1 < cols and is_a_path(x, y + 1, path_sum + cur_price)
          )
      res = is_a_path(0, 0, 0)
      return res
        
    