class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zeros = set()
        columns_with_zeros = set()
        for row in range(len(matrix)):
          for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
              rows_with_zeros.add(row)
              columns_with_zeros.add(col)
        
        for row in rows_with_zeros:
          for col in range(len(matrix[0])):
            matrix[row][col] = 0
        for col in columns_with_zeros:
          for row in range(len(matrix)):
            matrix[row][col] = 0
        return matrix