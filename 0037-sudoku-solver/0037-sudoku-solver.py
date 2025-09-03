class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
      board = board
      """
      Do not return anything, modify board in-place instead.
      """
      def free_in_row(row):
        available_nums = [True] * 9
        for value in board[row]:
          if value != '.':
            available_nums[int(value) - 1] = False
        return available_nums
      def free_in_col(col):
        available_nums = [True] * 9
        for row in board:
          val = row[col]
          if val != '.':
            available_nums[int(val) - 1] = False
        return available_nums

      def free_in_cell(cell_idx):
        min_row, max_row = (cell_idx // 3) * 3, (cell_idx // 3) * 3 + 3
        min_col, max_col = (cell_idx % 3) * 3, (cell_idx % 3) * 3 + 3
        available_nums = [True] * 9

        for row in range(min_row, max_row):
          for col in range(min_col, max_col):
            val = board[row][col]
            if val != '.':
              available_nums[int(val) - 1] = False
        return available_nums

      def get_cell_idx(row, col):
        vertical_idx = row // 3
        horizonal_idx = col // 3
        return vertical_idx * 3 + horizonal_idx


      allowed = [{},{},{}]
      def get_allowed_options(row, col):
        if not row in allowed[0]:
          allowed[0][row] = free_in_row(row)
        row_allowed = allowed[0][row]
        if not col in allowed[1]:
          allowed[1][col] = free_in_col(col)
        col_allowed = allowed[1][col]
        cell = get_cell_idx(row, col)
        if not cell in allowed[2]:
          allowed[2][cell] = free_in_cell(cell)
        cell_allowed = allowed[2][cell]
        res = []
        for idx in range(9):
          if row_allowed[idx] and col_allowed[idx] and cell_allowed[idx]:
            res.append(idx + 1)
        return res

      q = []
      for row in range(9):
        for col in range(9):
          if board[row][col] == '.':
            q.append((row, col))
      def add_to_used(row, col, val):
        val -= 1
        allowed[0][row][val] = False
        allowed[1][col][val] = False
        cell_idx = get_cell_idx(row, col)
        allowed[2][cell_idx][val] = False
        board[row][col] = str(val + 1)

      def remove_from_used(row, col, val):
        val -= 1
        allowed[0][row][val] = True
        allowed[1][col][val] = True
        cell_idx = get_cell_idx(row, col)
        allowed[2][cell_idx][val] = True
        board[row][col] = '.'

      def backtrack(cur_cell):
        if cur_cell == len(q):
          return True
        cur_row, cur_col = q[cur_cell]
        opts = get_allowed_options(cur_row, cur_col)
        for v in opts:
          add_to_used(cur_row, cur_col, v)
          is_solved = backtrack(cur_cell + 1)
          if is_solved:
            return True
          remove_from_used(cur_row, cur_col, v)
      backtrack(0)
          
      