class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_store = [set() for _ in range(9)]
        column_store = [set() for _ in range(9)]
        segment_storage = [set() for _ in range(9)]

        for row in range(len(board)):
          for column in range(len(board[0])):
            candidate = board[row][column]
            if candidate.isdigit():
              segment = 3 * (row // 3) + column // 3
              if candidate in row_store[row] or candidate in column_store[column] or candidate in segment_storage[segment]:
                return False
              row_store[row].add(candidate)
              column_store[column].add(candidate)
              segment_storage[segment].add(candidate)
        return True

        