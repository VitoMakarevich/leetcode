class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_store = [0 for _ in range(9)]
        column_store = [0 for _ in range(9)]
        segment_storage = [0 for _ in range(9)]
        def i_ex(num, i):
          return num & 1 << i
        def i_s(num, i):
          return num | 1 << i

        for row in range(len(board)):
          for column in range(len(board[0])):
            candidate = board[row][column]
            if candidate.isdigit():
              candidate = int(candidate)
              segment = 3 * (row // 3) + column // 3
              if i_ex(row_store[row], candidate) or i_ex(column_store[column], candidate) or i_ex(segment_storage[segment], candidate):
                return False
              row_store[row] = i_s(row_store[row], candidate)
              column_store[column] = i_s(column_store[column], candidate)
              segment_storage[segment] = i_s(segment_storage[segment], candidate)
        return True
    
        