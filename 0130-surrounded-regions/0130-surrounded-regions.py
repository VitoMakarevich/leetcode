class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for j in range(len(board)):
          for i in range(len(board[0])):
            item = board[j][i]
            if item == 'O':
              visited = set()
              res = self._check_neighbors(board, visited, i, j)
              if res:
                for v in visited:
                  vis_i, vis_j = v
                  board[vis_j][vis_i] = 'X'
                



    def _check_neighbors(self, board, visited, i, j):
      visited.add((i, j))
      neighbors = self._get_neighbors(board, i, j)
      if len(neighbors) < 4:
        return False
      for v in neighbors:
        i_neighbor, j_neighbor = v
        if (i_neighbor, j_neighbor) not in visited and board[j_neighbor][i_neighbor] == 'O':
          res = self._check_neighbors(board, visited, i_neighbor, j_neighbor)
          if not res:
            return False
      return True
    def _get_neighbors(self, board, i, j):
      res = []
      if i - 1 >= 0:
        res.append((i - 1, j))
      if i + 1 < len(board[0]):
        res.append((i + 1, j))
      if j - 1 >= 0:
        res.append((i, j - 1))
      if j + 1 < len(board):
        res.append((i, j + 1))
      return res