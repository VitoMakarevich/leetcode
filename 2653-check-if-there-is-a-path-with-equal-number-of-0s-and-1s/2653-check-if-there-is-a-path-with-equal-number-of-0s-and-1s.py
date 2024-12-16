class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
      self._grid = grid
      @cache
      def is_a_path(x, y, path_sum):
        cur_price = -1 if self._grid[x][y] == 0 else 1
        if x == len(self._grid) - 1 and y == len(self._grid[0]) - 1:
          return path_sum + cur_price == 0
        else:
          return (x + 1 < len(self._grid) and is_a_path(x + 1, y, path_sum + cur_price)) or (
            y + 1 < len(self._grid[0]) and is_a_path(x, y + 1, path_sum + cur_price)
          )
      res = is_a_path(0, 0, 0)
      return res
        
    