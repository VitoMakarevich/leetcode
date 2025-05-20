class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['f'] * n for _ in range(m)]
        for i, j in walls:
          matrix[i][j] = 'w'
        for i, j in guards:
          matrix[i][j] = 'g'
        
        
        free_cells = m * n - len(guards) - len(walls)
        for i, j in guards:
          directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
          for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            while 0 <= next_i < m and 0 <= next_j < n and (matrix[next_i][next_j] == 'f' or  matrix[next_i][next_j] == 'o'):
              used_count = int(matrix[next_i][next_j] == 'f')
              free_cells -= used_count
              matrix[next_i][next_j] = 'o'
              next_i, next_j = next_i + direction[0], next_j + direction[1]
        return free_cells
