class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        dirs = {
          'r': 'b',
          'b': 'l',
          'l': 'u',
          'u': 'r'
        }
        last_processed = {
          'r': len(matrix[0]),
          'b': len(matrix),
          'l': -1,
          'u': -1
        }

        def process(row, col, direction):
          if row == last_processed['u'] or row == last_processed['b'] or col == last_processed['l'] or col == last_processed['r']:
            return
          border = last_processed[direction]
          next_dir = dirs[direction]
          if direction == 'r':
            last_processed['u'] += 1
            for i in range(col, border):
              res.append(matrix[row][i])
            process(row + 1, border - 1, next_dir)
          elif direction == 'b':
            last_processed['r'] -= 1
            for i in range(row, border):
              res.append(matrix[i][col])
            process(border - 1, col - 1, next_dir)
          elif direction == 'l':
            last_processed['b'] -= 1
            for i in range(col, border, -1):
              res.append(matrix[row][i])
            process(row - 1, border + 1, next_dir)
          elif direction == 'u':
            last_processed['l'] += 1
            for i in range(row, border, -1):
              res.append(matrix[i][col])
            process(border + 1, col + 1, next_dir)
        process(0, 0, 'r')
        return res
          

